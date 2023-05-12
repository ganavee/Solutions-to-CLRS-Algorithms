def palindrome(string, start, end):
    if(start >= end):
        return True
    if(string[start] == string[end]):
        return palindrome(string, start+1, end-1)
    else:
        return False


string = input("Enter the string: ")
print(f"String {string} is Palindrome?: {palindrome(string, 0, len(string)-1)}")
