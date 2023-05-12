#PowerSet

#Recursion
#TC =  O(2^n)*n
#SC = O(n)
def subseq(string, seq, arr):
    if(seq == ""):
        arr.append(string)
        return arr
    popChar = seq[-1]
    seq = seq[:-1]
    subseq(popChar + string, seq, arr)
    subseq(string, seq, arr)
    return arr


seq = input("Enter the subsequence: ")
arr = []
string = ""
print(f"Subsequences of {seq} is {subseq(string, seq, arr)}")
