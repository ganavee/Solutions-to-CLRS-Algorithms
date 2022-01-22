''' Insertion sort using recursive approach'''

#To insert a given element at the right position

def insert(A, ele, end_ind):
    end_ind -= 1
    extra = A[end_ind]
    while(end_ind >= 0 and extra > ele):
            A[end_ind + 1] = extra
            end_ind -= 1
            extra = A[end_ind]
    A[end_ind + 1] = ele
        

def insertion_sort(A, n):
    if(n>1):
        ele = A[n-1]
        insertion_sort(A, n-1)
        insert(A, ele, n-1)

A = [3, 41, 52, 26, 38, 57, 9, 49]
insertion_sort(A,len(A))
print("Sorted Array: ", A)
