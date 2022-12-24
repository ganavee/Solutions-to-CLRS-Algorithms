#Cyclic sort
def sort(a):
    length = len(a)
    index = 0
    while(index < length):
        if(a[index] != (index + 1)):
            temp = a[index]
            a[index] = a[a[index] - 1]
            a[temp - 1] = temp
        else:
            index += 1
    print("Sorted Array ", a)

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [3, 4, 2, 5, 1]
sort(c)
