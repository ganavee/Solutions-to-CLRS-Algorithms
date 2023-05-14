 
#Printing the subsequnce whose sum is k
def newSeq(subSum, subTup, tup, k, arr, count):
    #print(f"subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    if(len(tup) == 0):
        if(subSum == k):
            arr.append(subTup)
            count += 1
        return count
    ele = tup[0]
    newTup = tup[1:]
    del tup
    #print(f"First{i}: subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    count = newSeq(subSum, subTup, newTup, k, arr, count)
    newSubTup = subTup + (ele, )
    del subTup
    #print(f"Second{i}: subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    count = newSeq(subSum+ele, newSubTup, newTup, k, arr, count)
    return count

#Works for single digit number
def subseq1(sumString, string, seq, arr, k):
    if(seq == ""):
        if(sumString == k):
            arr.append(string)
        return arr
    popChar = seq[-1]
    popNum = int(popChar)
    seq = seq[:-1]
    subseq1(sumString, string, seq, arr, k)
    subseq1(popNum + sumString, popChar + string, seq, arr, k)
    return arr

print ("\n" * 100)
seq = [int(i) for i in input("Enter the subsequence: ").split(",")]
k = int(input("Enter the value of k: "))
arr = []
seq = tuple(seq)
print(f"Subsequence of {seq} whose sum is equal to {k} is {newSeq(0, (), seq, k, arr, 0)}")

