import sys
import csv

# getFileContents
#
# Retreives file contents of given input file and formats it as an array
#
# @filePath Path to file containing algorithm input
# @return Contents of input file as array
def getFileContents(filePath):
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        fileContents = list(reader)
    return fileContents

# ???
def recursiveSolve(q, qCompare, p, intersections):
    for qIndex in range(qCompare, len(p)):
        if(int(p[qIndex]) < int(p[qCompare])):
            intersections += 1
    if(qCompare + 1 < len(p)):
        return recursiveSolve(q, qCompare + 1, p, intersections)

    return intersections

def main():
    fileContents = getFileContents(sys.argv[1])
    pointCount = int(fileContents[0][0])
    q = fileContents[1]
    p = fileContents[2]
    intersections = 0

    print recursiveSolve(q, 0, p, intersections)

if __name__ == '__main__':
  main()
