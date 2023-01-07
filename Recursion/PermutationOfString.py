#Find all the permutations of the given string


def permutations(s, processed):
    res = []
    if(s == ""):
        res.append(processed)
        return res
    
    char = s[0]
    
    for pos in range(len(processed) + 1):
        string = processed[0:pos] + char + processed[pos:]
        result = permutations(s[1:], string)
        res.extend(result)
    return res 
        


    


s = "abc"
res = []
print(permutations(s, ""))


