b = [15, 25, 35, 45, 5, 5, 25]
a = [45, 5, 65, 75, 85, 75,45]

def intersection_using_dic():
    D1 = {}
    for i in a:
        D1[i] = 1
    c = []
    D2 = {}
    for i in b:
        D2 [i] = 1
    for i in D1.keys():
        if i in D2:
            c.append(i)
    print("The intersection of two lists is ", c)

def union_using_dic():
    D = {}
    u = []
    for i in a:
        if i not in D:
            u.append(i)
            D[i] = 1
    for i in b:
        if i not in D:
            u.append(i)
            D[i] = 1
    print("The union of two lists is ", u)

def difference():
    D1 = {}
    D2 = {}
    c = []
    for i in b:
        D2[i] = 1
    for i in a:
        D1[i] = 1
    for i in D1.keys():
        if i not in D2:
            c.append(i)
    print("A - B = ", c)

def symmetric_difference():
    D1 = {}
    D2 = {}
    c = []
    for i in a:
        D1[i] = 1
    for i in b:
        D2[i] = 1
    for i in D1.keys():
        if i not in D2:
            c.append(i)
    for i in D2.keys():
        if i not in D1:
            c.append(i)
    print("Symmetric Difference is ", c)

intersection_using_dic()
union_using_dic()
difference()
symmetric_difference()
