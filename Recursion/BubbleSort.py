#Bubble sort usng Recursion


def sorting(a, firstPass, secondPass):
    #print(a, firstPass, secondPass)
    if(firstPass == 0):
        return
    if(secondPass == firstPass + 1):
        #print("After 1 pass ", a)
        secondPass = 1
        firstPass -= 1
    if(a[secondPass - 1] > a[secondPass]):
        swap = a[secondPass - 1]
        a[secondPass - 1] = a[secondPass]
        a[secondPass] = swap
    return sorting(a, firstPass, secondPass + 1)
    


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [10, 45, 21, 0, -9, -27, 12568, 32]
d = [5, 4, 1, 2, 3]
sorting(c, len(c)-1, 1)
print(c)
