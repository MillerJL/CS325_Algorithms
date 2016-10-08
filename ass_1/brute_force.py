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

def main():
    fileContents = getFileContents(sys.argv[1])
    pointCount = int(fileContents[0][0])
    q = fileContents[1]
    p = fileContents[2]
    intersections = 0

    for qIndex in range(0, pointCount):
        # print 'Loop: ' + str(qIndex)
        for q2Index in range(qIndex + 1, pointCount):
            intersections += 1
        print intersections
            # if(int(p[q2Index]) < int(p[qIndex])):
            #     intersections += 1
    print intersections

if __name__ == '__main__':
  main()
