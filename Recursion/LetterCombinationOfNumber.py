def recursion(d, up, p, res):
    if(up == ""):
        res.append(p)
        return res
    string = d[up[0]]
    for i in string:
        res = recursion(d, up[1:], p+i, res)
    return res
        


d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs",
     "8": "tuv", "9": "wxyz"}
num = ""

res = []
val = recursion(d, num, "", res)
)
