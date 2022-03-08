a = [15, 25, 35, 45, 5]
b = [45, 5, 65, 75, 85]

def intersection_using_dic():
    D = {}
    for i in a:
        D[i] = 1
    union = []
    for i in b:
        if i in a:
            union.append(i)
    print(union)

def 

intersection_using_dic()
