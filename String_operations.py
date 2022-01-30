"""Basic String Operations Implementation"""

'''To find the lenght of the string'''
def length(s):
    count = 0
    for i in s:
        count += 1
    print("The length of the string is ", count)

'''To find a character in the string'''
def find_char(s, ch):
    if(len(ch) > 1):
        print("This function is only for character")
        exit()
    for i in range(len(s)):
        if(ch == s[i]):
            print("Found char {0} at index {1}".format(ch, i))
            break
    else:
        print("Ch = {0} not found".format(ch))

'''To find a substring in the string'''
def find_substring(s, ss):
    length = len(s) - len(ss) + 1
    if(len(ss) == 0):
        print("Please enter valid string")
        exit()
    for i in range(length):
        for j in range(len(ss)):
            if(i+j < len(s) and ss[j] != s[i+j]):
                break
        else:
            print("Substring {0} found at index {1}".format(ss, i))
            break
    else:
        print("Substring not found")


s = "catdogranpig"
p = "ran"
empty = ""
length(p)
find_substring(s, '')
