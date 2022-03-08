a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

def union_using_dic():
    D = {}
    for i in a:
        D[i] = 1
    union = []
    for i in b:
        if i in a:
            union.append(i)
    print(union)

union_using_dic()
