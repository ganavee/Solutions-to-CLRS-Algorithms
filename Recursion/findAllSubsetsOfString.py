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



s = "abc"
print(subset(s, ""))
