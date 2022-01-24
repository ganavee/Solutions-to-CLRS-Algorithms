A = [5, 2, 4, 6, 1, 3]


def solution1():
    for j in range(len(A)-1):
        small = A[j]
        i = j + 1
        ind = j
        while(i <= len(A) - 1):
            if(small > A[i]):
                ind = i
                small = A[i]
            i += 1
        A[ind] = A[j]
        A[j] = small
    print("The sorted array is ", A)

solution1()
