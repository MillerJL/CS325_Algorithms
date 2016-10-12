# CS325 - Group Assignment1
# 2016-10-11
# John Miller, Shane Barrantes, Griffin Gonsalves, Steven Powers
#
# Finds the solution to the line intersections problem in nlog(n) runtime

import sys
import csv
import time

def getFileContents(filePath):
    """ Gets the contents of an input file and return it
    filePath -- Path to the input file containing test data
    """
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        fileContents = list(reader)
    return fileContents

def writeOutputFile(value):
    f = open('output.txt', 'w')
    f.write(str(value))
    f.close()

def mergeSort(arr, beg, end):
    """ Recursive Merge Sort algorithm used as basis for solution to line intersection problem and
        returns the number of line intersections
    arr -- Array containing input data. Should be 'p' values (third line of input file)
    beg -- Index of the 'start' of the array
    end -- Index of the 'end' of the array
    """
    # Count of values moved in left half of original array
    left = 0
    # Count of values moved in right half of original array
    right = 0
    # Count of values moved while merging left and right halfs of original array
    count = 0
    mid = 0

    if beg < end:
        mid = (beg + end) / 2
        left = mergeSort(arr, beg, mid)
        right = mergeSort(arr, mid + 1, end)
        count = merge(arr, beg, mid, end)

    return left + right + count

def still_merging(left, right, mid, end):
    """ Checks to see if the algorithm should still be merging the two target arrays together and
        returns true/false if it should/shouldn't
    left -- The index of the current value being compared in the left array
    right -- The index of the current value being compared in the right array
    mid -- The 'end' of the left array
    end -- The 'end' of the right array
    """
    return left <= mid and right <= end

def merge(arr, beg, mid, end):
    """ Merges two given array and returns the number of positions a value in the
        'right' array has to move when merging into the 'left' array
    arr -- Array containing input data. Should be 'p' values (third line of input file)
    beg -- Index of the 'start' of the array
    mid -- The 'end' of the left array
    end -- The 'end' of the right array
    """
    # Temporary array used to store merged values
    tempArr = [0] * len(arr)
    # Current index being examined in the 'left' array
    left = beg
    # Current index being examined in the 'right' array
    right = mid + 1
    # Index used to track where sorted values should be placed in tempArr
    cur = left
    intersections = 0

    while still_merging(left, right, mid, end):
        if arr[left] <= arr[right]:
            tempArr[cur] = arr[left]
            left += 1
        else:
            intersections += (right - cur)
            tempArr[cur] = arr[right]
            right += 1
        cur += 1

    while left <= mid:
        tempArr[cur] = arr[left]
        cur += 1
        left += 1

    while right <= end:
        tempArr[cur] = arr[right]
        cur += 1
        right += 1

    for i in range(beg, end + 1):
        arr[i] = tempArr[i]

    return intersections

file_list = [
    'data/100.txt',
    'data/500.txt',
    'data/1000.txt',
    'data/2000.txt',
    'data/5000.txt',
    'data/10000.txt'
]

for dataFile in file_list:
    totalTime = 0.0
    for i in range(0, 10):
        fileContents = map(int, getFileContents(dataFile)[0])
        start_time = time.time()
        num_intersections = mergeSort(fileContents, 0, len(fileContents) - 1)
        totalTime += (time.time() - start_time)/10
    print("%s" % ((totalTime) / 10))
        # print("%s" % ((time.time() - start_time)/10))
