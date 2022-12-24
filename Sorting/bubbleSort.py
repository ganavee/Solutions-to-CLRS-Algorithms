#Bubble sort

def sort(a):
    length = len(a) - 1
    for i in range(length, -1, -1):
        isSorted = True
        for j in range(1, i+1):
            if(a[j-1] > a[j]):
                isSorted = False
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
        if(isSorted):
            break
        print("pass ", a)
    print("Sorted Array is ",a)

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [10, 45, 21, 0, -9, -27, 12568, 32]
d = [5, 4, 1, 2, 3]
sort(d)
