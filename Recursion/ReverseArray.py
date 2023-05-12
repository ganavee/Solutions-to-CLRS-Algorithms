#TC O(n)
#SC O(N)
#Reversing Array
#Two Pointer
def reverse1(arr, start, end):
    if(start >= end):
        return arr
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    return reverse1(arr, start+1, end-1)

#SinglePointer
def reverse2(arr, start):
    end = len(arr)-1-start
    if(start >= end):
        return arr
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    return reverse2(arr, start+1)
    
while(True):
    try:
        arr = [int(x) for x in input("Enter array separated by comma(Minimum 1 element): ").split(",")]
        break
    except:
        print("The Array you entered does not meet the requirements")
print("Array is ", arr)
print(f"First: Array {arr} after reversing is {reverse1(arr, 0, len(arr)-1)}")
print(f"Second: Array {arr} after reversing is {reverse2(arr, 0)}")
