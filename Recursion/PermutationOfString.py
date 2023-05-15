def permute(subString, string, result):
    if(len(string) == 0):
        result.append(subString)
        return result
    for i in range(len(string)):
        permute(subString + string[i], string[0:i] + string[i+1:], result)
    del string
    del subString
    return result


string = "abcd"
result = []
print("Result = ", permute("", string, result))
