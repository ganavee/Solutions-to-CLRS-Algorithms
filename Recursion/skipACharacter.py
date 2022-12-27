#Skip a character using Recursion

def skip(string, char, res, index):
    if(index == len(string)):
        return res
    if(string[index] != char):
        res.append(string[index])
    return skip(string, char, res, index+1)
    

string = "baccad"
char = 'a'
res = []
print(''.join(skip(string, char, res, 0)))
