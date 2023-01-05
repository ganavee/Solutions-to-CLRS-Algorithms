#Subsets of a string


def subset(s, processed):
    res = []
    if(s == ""):
        return processed
    val1 = subset(s[1:], processed + s[0])
    val2 = subset(s[1:], processed)
    #print(val1, val2)
    if(type(val1)) is list:
        res.extend(val1)
    elif(val1 != ""):
        res.append(val1)
    if(type(val2)) is list:
        res.extend(val2)
    elif(val2 != ""):
        res.append(val2)
    return res



s = "abc"
print(subset(s, ""))
