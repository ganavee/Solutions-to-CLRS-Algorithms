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

'''to convert a given string into list'''
def convert_to_list(s):
    ch = []
    for i in (s):
        ch.append(i)
    print("The character array is ", ch)
    convert_to_string(ch)
    return ch

'''Convert given list to string'''
def convert_to_string(li):
    s = ""
    for i in li:
        s += i
    print("String is ", s)


'''Concatenation of string'''
def concat(s, s1):
    for i in s1:
        s += i
    print("The new concatenated string is ", s)
  

'''Slicing of given string'''
def slicing(s, start=0, end=None):
    if end is None:
        end = len(s)
    ss = ""
    if(end < 0):
        end = len(s) + end
    for i in range(start, end):
        ss += s[i]
    print("The sliced string is ", ss)

'''Extended Slicing'''
def extended_slicing(s, start = None, end =  None, stride = None):
    ss = ""
    if(stride >= 0):
        if start is None:
            start = 0
        if end is None:
            end = len(s)
        for i in range(start, end, stride):
            print(i)
            ss += s[i]
    else:
        if start is None:
            start = len(s)-1
        if end is None:
            end = 0
        for i in range(start, end, stride):
            ss += s[i]
    print("New string is ", ss)
        

'''Replace given string  with all occurence of the matchingsubstring'''
def replace_substring(s, old_ss, new_ss):
    length = len(s)- len(old_ss) +1
    search_start = 0
    while(search_start < len(s)):
        count = 0
        #to find all the substring
        for j in range(len(old_ss)):
            if(old_ss[j] != s[search_start+j]):
                break
            else:
                count += 1
        #To replace old with new substring
        if(count == len(old_ss)):
            print("Found at index", search_start)
            first = s[0:search_start]
            first += new_ss
            first += s[search_start+len(old_ss):len(s)]
            s = first
            search_start += len(new_ss)
        else:
             search_start += 1
    print("New string ", s)

'''to convert all the characters to uppercase'''
def to_uppercase(s):
    new_str = ""
    for i in s:
        asc = ord(i)
        if(asc>= 97 and asc<= 122):
            asc -= 32
            new_str += chr(asc)
        else:
            new_str += i            
    print("Upper case string is ", new_str)

'''to check is all the characters in the string are in uppercase'''
def is_uppercase(s):
    new_str = ""
    for i in s:
        asc = ord(i)
        if(asc>= 97 and asc<= 122):
            print("All the characters in the string is not in UpperCase")
            break
    else:
        print("The string is in UpperCase")

'''to convert all the characters to lowercase'''
def to_lowercase(s):
    new_str = ""
    for i in s:
        asc = ord(i)
        if(asc>= 65 and asc<= 90):
            asc += 32
            new_str += chr(asc)
        else:
            new_str += i            
    print("Lower case string is ", new_str)

'''to check is all the characters in the string are in lowercase'''
def is_lowercase(s):
    new_str = ""
    for i in s:
        asc = ord(i)
        if(asc>= 65 and asc<= 90):
            print("All the characters in the string is not in LowerCase")
            break
    else:
        print("The string is in LowerCase")


'''swapcase'''
def swap_case(s):
    new_str = ""
    for i in s:
        asc = ord(i)
        if(asc>= 65 and asc<= 90):
            asc += 32
            new_str += chr(asc)
        elif(asc>= 97 and asc<= 122):
            asc -= 32
            new_str += chr(asc)
        else:
            new_str += i
    print("New string is ", new_str)

    
'''To check if the given string is alphanumeric'''
def is_alpha(s):
    for i in s:
        asc = ord(i)
        if(not((asc >=65 and asc <= 90) or (asc >=97 and asc <= 122) or (asc >=48 and asc <= 57))):
            print("The given string is not alphanumeric ")
            break
    else:
        print("The given string is alphanumeric")
    

'''To check if the given string is decimal'''
def is_decimal(s):
    if(s%1 == 0):
        print("Not decimal")
    else:
        print("The given number is decimal")

'''To check if the given string is digit'''
def is_digit(s):
    for i in s:
        asc = ord(i)
        if(not(asc >=48 and asc <= 57)):
            print("The given string is not numeric ")
            break
    else:
        print("The given string is numeric")

'''To check if the string is starts with with a given string'''
def startswith(s, ss):
    if (len(ss) > len(s)):
        print("The given string does not start with ", ss)
        exit()
    for i in range(len(ss)):
        if(s[i] != ss[i]):
            print("The given string does not start with ", ss)
            break
    else:
        print("The given string starts with ", ss)
  

'''To check if the string is ends with with a given string'''
def endswith(s, ss):
    if (len(ss) > len(s)):
        print("The given string does not end with ", ss)
        exit()
    length = len(s) - len(ss)
    for i in range(len(ss)):
        if(ss[i] != s[length + i]):
            print("The given string does not end with ", ss)
            break
    else:
        print("The given string end with ", ss)

'''To check is the string begins with whitespaces'''
def l_strip(s):
    if((s[0]) == ' '):
        print("The given string starts with whitespaces")
    else:
        print("The given string does not start with whitespaces")

'''To split the string based on the separator'''
def split(s, separator):
    lst = []
    start = 0
    s.rstrip()
    for i in range(len(s)):
        if(s[i] == separator and i!=len(s)-1):
            lst.append(s[start:i])
            start = i+1
    lst.append(s[start:len(s)])
    print("The new string is ", lst)


s = "   catdogran23GPA$pigza"
q = "RMA123zaZA09"
r = "SPA"
p = "rcranpitran"
empty = ""
split("Hello.how.are you", ".")
#r_strip(q)
#endswith(s, "a$pigza")
#startswith(s, "cato")
#is_decimal(19.03)
#is_digit("12309")
#is_alpha(s)
#swap_case(q)
#to_lowercase(empty)
#to_uppercase(s)
#replace_substring(empty, "ran", "porting")
#extended_slicing(s, start = 12, end = 5, stride = 2)
#slicing("spam", end = -2)
#concat(empty, "hello")
#convert_to_list(s)
#find_substring(s, '')
#length(p)

