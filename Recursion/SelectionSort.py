#Selection sort using Recursion


def sorting(a, insertIndex, startIndex, smallestIndex, length):
    if(insertIndex == length - 1):
        return
    if(startIndex == length + 1):
        swap = a[insertIndex]
        a[insertIndex] = a[smallestIndex]
        a[smallestIndex] = swap
        insertIndex += 1
        startIndex = insertIndex + 1
        smallestIndex = insertIndex
    if(a[smallestIndex] > a[startIndex]):
        smallestIndex = startIndex
    return sorting(a, insertIndex, startIndex + 1, smallestIndex, length)
    

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [10, 45, 21, 0, -9, -27, 12568, 32]
d = [5, 4, 1, 2, 3]
sorting(d, 0, 1, 0, len(d)-1)
print(d)


