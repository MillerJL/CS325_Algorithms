# CS325 - Group Assignment2
# 2016-10-23
# John Miller, Shane Barrantes
#
# Recursive solution to the frog jumping problem. Finds the smallest leash in
# the given set of leashes that can successfully allow the frogs to get to their
# destinations
#
# Usage: python jump.py *path_to_input_file*
# Outputs: File containing number of intersections called output.txt
#
# Requires file format provided in assignment description. CSV format
# Line 1 of the input is a single integer 1 <= m <= 1000.
# Line 2 specifies P. It is a list of m points (pair of integers) separated by
#        commas. Line 3 of the input is a single integer 1 <= n <= 1000.
# Line 4 specifies Q. It is a list of n points (pair of integers) separated by commas.
# Line 5 of the input is a single integer 1 <= t <= 1000. Line 6 specifies L.
#        It is a list of t integers separated by commas

import math
import ast
import sys

# Lets our code actually run
sys.setrecursionlimit(10000000)

# Retreives and formats the contents of the provided file.
# Returns a list that can be searched. List is in same format as the file input.
def getFileContents(filePath):
    result = []

    with open(filePath, 'r') as f:
        for line in f:
            result.append(line)

    result[0] = result[0][0]
    result[1] = ast.literal_eval('[{0}]'.format(result[1]))
    result[2] = result[2][0]
    result[3] = ast.literal_eval('[{0}]'.format(result[3]))
    result[4] = result[4][0]
    result[5] = map(int, result[5].split(','))
    return result

# Writes the result of the algorithm to 'output.txt'
# This should contain a single integer value (the shortest leash) or False
#   if there is no viable leash in the list of given leashes
def writeOutputFile(value):
    f = open('output.txt', 'w')
    f.write(str(value))
    f.close()

# Finds the distance between two points in a matrix
def distance(P, Q):
    return int(math.ceil(math.hypot((abs(P[0] - Q[0])), (abs(P[1] - Q[1])))))

# Recursive algorithm that finds a viable path if there is one, given a specific
# leash length
#
# returns true if there it is possible, false if it is not
def Jump(P, Q, leash):
    # Length of current possible P moves left
    P_len = len(P) - 1
    # Length of current possible Q moves left
    Q_len = len(Q) - 1

    if distance(P[P_len], Q[Q_len]) > leash:
        return False

    if P_len == 0 and Q_len == 0:
        return True

    if (P_len > 0 and Q_len > 0) and distance(P[P_len - 1], Q[Q_len - 1]) <= leash:
        return Jump(P[0:P_len], Q[0:Q_len], leash)

    if P_len > 0 and distance(P[P_len - 1], Q[Q_len]) <= leash:
        return Jump(P[0:P_len], Q, leash)

    if Q_len > 0 and distance(P[P_len], Q[Q_len - 1]) <= leash:
        return Jump(P, Q[0:Q_len], leash)

    return False

# Read file contents in and format it
fileContents = getFileContents(sys.argv[1])

L = fileContents[5]
L.sort()

i = 0
bestLeash = False
L_length = int(len(L))

while(L_length >= 1):
    L_length = int(len(L))
    i = int(math.ceil(len(L)/2))
    result = Jump(fileContents[1], fileContents[3], L[i])

    if result == False:
        L = L[i:len(L)]
    else:
        bestLeash = L[i]
        L = L[0:i]
    L_length = (L_length - int(len(L)))

writeOutputFile(bestLeash)
