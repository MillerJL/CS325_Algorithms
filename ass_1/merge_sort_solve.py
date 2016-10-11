import sys
import csv

def getFileContents(filePath):
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        fileContents = list(reader)
    return fileContents

def mergeSort(arr, beg, end):
    left = 0
    right = 0
    count = 0
    mid = 0

    if beg < end:
        mid = (beg + end) / 2
        left = mergeSort(arr, beg, mid)
        right = mergeSort(arr, mid + 1, end)
        count = merge(arr, beg, mid, end)

    return left + right + count

def still_merging(left, right, mid, end):
    return left <= mid and right <= end

def merge(arr, beg, mid, end):
    tempArr = [0] * len(arr)
    left = beg
    right = mid + 1
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

fileContents = map(int, getFileContents(sys.argv[1])[2])
print mergeSort(fileContents, 0, len(fileContents) - 1)
