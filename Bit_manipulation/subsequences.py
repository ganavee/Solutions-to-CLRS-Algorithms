string = "abc"
length = len(string)
result = []
for i in range(pow(2, length)):
    sub= ""
    for j in range(length):
        if(i & i<<j):
            sub +=  string[j]
    result.append(sub)
print("subsequences are ", result)
