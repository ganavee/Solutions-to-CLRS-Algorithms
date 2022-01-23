def rec_binary_search(A, start, end, ele):
    if(start <= end):
        mid = (start + end) //2
        if(A[mid] == ele):
            print("Element found at {0}".format(mid + 1))
            return
        elif(A[mid] > ele):
            rec_binary_search(A, start, mid-1, ele)
        elif(A[mid] < ele):
            rec_binary_search(A, mid+1, end, ele)
    else:
        print("Element not found")
            
def iterative_binary_search(A, start, end, ele):
    while(start <= end):
        mid = (start + end) // 2
        if(A[mid] == ele):
            print("Element found at {0}".format(mid + 1))
            break
        elif(A[mid] > ele):
            end = mid - 1
        elif(A[mid] < ele):
            start = mid + 1
    else:
        print("Element not found")
    
A = [4, 11, 23, 46, 75, 99, 105]
rec_binary_search(A, 0, len(A)-1, 46)
