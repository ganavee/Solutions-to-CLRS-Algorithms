#Check if the array is sorted or not using Recursion

a = [4, 6, 123, 567, 578, 78]

def sortedArray(a, index):
    if(index == len(a)):
        return True
    if(a[index] < a[index - 1]):
        return False
    return sortedArray(a, index + 1)


print(sortedArray(a, 1))
