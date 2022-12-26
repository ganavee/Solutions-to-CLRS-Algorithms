#Merge sort using Recursion


def merge(a, start, mid, end):
    first = start
    second = mid + 1
    res = []
    while(first <= mid and second <= end):
        if(a[first] < a[second]):
            res.append(a[first])
            first += 1
        else:
            res.append(a[second])
            second +=1
    while(first <= mid):
        res.append(a[first])
        first += 1
    while(second <= end):
        res.append(a[second])
        second += 1
    for i in res:
        a[start] = i
        start += 1


def mergeSort(a, start, end):
    if(start == end):
        return
    mid = (start + end ) // 2
    mergeSort(a, start, mid)
    mergeSort(a, mid + 1, end)
    merge(a, start, mid, end)


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [10, 45, 21, 0, -9, -27, 12568, 32]
d = [5, 4, 1, 2, 3]
e = [38, 27, 43, 3, 9, 82, 10]
length = len(d)
mergeSort(d, 0, length-1)
print(d)
