import math
import ast
import sys

sys.setrecursionlimit(10000000)


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


def Jump(P, Q, leash):
    P_len = len(P) - 1
    Q_len = len(Q) - 1

    if distance(P[P_len], Q[Q_len]) > leash:
        return False

    if P_len == 0 and Q_len == 0:
        return True

    if (P_len > 0 and Q_len > 0) and (distance(P[P_len - 1], Q[Q_len - 1]) <= leash):
        return Jump(P[0:P_len], Q[0:Q_len], leash)

    if P_len > 0 and (distance(P[P_len - 1], Q[Q_len]) <= leash):
        return Jump(P[0:P_len], Q, leash)

    if Q_len > 0 and (distance(P[P_len], Q[Q_len - 1]) <= leash):
        return Jump(P, Q[0:Q_len], leash)

    return False


def distance(P, Q):
    return int(math.ceil(math.hypot((abs(P[0] - Q[0])), (abs(P[1] - Q[1])))))

fileContents = getFileContents(sys.argv[1])
print Jump(fileContents[1], fileContents[3], 10)
