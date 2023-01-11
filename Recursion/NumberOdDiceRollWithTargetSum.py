def recursion(target, up, p, res, total):
    if(total == target):
        res.append(p)
    if(total > target):
        return res
    for i in up:
        res = recursion(target, up, p+i, res, total+int(i))
    
    return res
    


target = 4
up = "123456"
res = []
print(recursion(target, up, "", res, 0))
