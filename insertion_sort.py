#To display the given array

def display(A):
    for i in range(0, len(A)) :
        print(A[i], end = " ")
    print()


#Sorting the given array in ascending order

def ascending_order(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while(j > -1 and A[j] > key):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    display(A)


#Sorting the given array in decending order

def descending_order(B):
    for i in range(1, len(B)):
        key = B[i]
        j = i - 1
        while( j >= 0 and B[j] < key):
            B[j+1] = B[j]
            j -= 1
        #if(B[j+1] < key):
            B[j+1] = key
    display(B)
        

A  =  [5, 2, 4, 6, 1, 3]
ascending_order(A)
descending_order(A)

