
#Printing the subsequnce whose sum is k
def newSeq(subSum, subTup, tup, k, arr, i, boolVal):
    #print(f"subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    if(len(tup) == 0):
        if(subSum == k):
            arr.append(subTup)
            boolVal = True
        return arr, boolVal
    ele = tup[0]
    newTup = tup[1:]
    del tup
    #print(f"First{i}: subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    arr, boolVal = newSeq(subSum, subTup, newTup, k, arr, i+1, boolVal)
    if(boolVal == True):
        return arr, boolVal
    newSubTup = subTup + (ele, )
    del subTup
    #print(f"Second{i}: subSum = {subSum} subTup = {subTup} tup = {tup}, arr = {arr}")
    arr, boolVal = newSeq(subSum+ele, newSubTup, newTup, k, arr, i+1, boolVal)
    return arr, boolVal


seq = [int(i) for i in input("Enter the subsequence: ").split(",")]
k = int(input("Enter the value of k: "))
arr = []
seq = tuple(seq)
print(f"Subsequence of {seq} whose sum is equal to {k} is {newSeq(0, (), seq, k, arr, 1, False)[0]}")

