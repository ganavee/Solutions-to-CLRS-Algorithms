A = [5, 4, 2, 6, 1, 3]

def linear_search(A, v):
    i = None
    for j in range(len(A)):
        if(A[j] == v):
            i = j
            break
    return i+1

value = 3
index = linear_search(A, value)
print("Index of value {0} is {1}".format(value, index))
