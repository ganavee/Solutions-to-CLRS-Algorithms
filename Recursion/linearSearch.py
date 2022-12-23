#Linear Search

def linear(a, ele, index):
    if(index == len(a)):
        return False
    if(a[index] == ele):
        return True
    return linear(a, ele, index + 1)

a = [5, 8, 9, 12, 56, 2, 890]
#print(linear(a, 891, 0))


def multipleLinear(a, ele, index, res):
    if(index == len(a)):
        return res
    if(a[index] == ele):
        res.append(index)
    return multipleLinear(a, ele, index + 1, res)
    

a = [5, 8, 9, 12, 56, 2, 890, 2]
res = []
#print(multipleLinear(a, 6, 0, res))


def mulLinearNoList(a, ele, index):
    res = []
    if(index == len(a)):
        return res
    if(a[index] == ele):
        res.append(index)
    ans = mulLinearNoList(a, ele, index + 1)
    res.extend(ans)
    return res

a = [2, 6, 890, 456, 12, 2, 890, 2]
print(mulLinearNoList(a, 4, 0))
