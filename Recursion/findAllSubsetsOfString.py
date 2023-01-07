#Subsets of a string


def subset(s, processed):
    res = []
    if(s == ""):
        res.append(processed)
        return res
    val1 = subset(s[1:], processed + s[0])
    val2 = subset(s[1:], processed)
    res.extend(val1)
    res.extend(val2)
    return res


def iterative(s):
    res = [[]]
    for i in s:
        res1 = []
        res1.extend(res)
        print("res1 before = ", res1)
        for j in res:
            print("j before = ", j)
            temp = []
            temp.extend(j)
            temp.append(i)
            print("j after = ", j)
            res1.append(temp)
            print("res1 after ",res1)
        res = res1
        print("res = ", res)
    print(res)


def duplicate(s):
    pass

s = "abc"
#print(subset(s, ""))
iterative(s)
