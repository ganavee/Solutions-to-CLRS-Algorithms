def seq(subSum, subTup, tup, target, index, arr, i):
        #print(f"subSum = {subSum} subTup = {subTup} tup = {tup} arr = {arr}")
        if(subSum == target):
            arr.append(list(subTup))
            return arr
        if(index >= len(tup) or subSum > target):
            return arr
        #choosing
        ele = tup[index]
        newSubTup = subTup + (ele, )
        #print(f"First{i}: subSum = {subSum+ele} subTup = {newSubTup} tup = {tup} arr = {arr}")
        seq(subSum + ele, newSubTup, tup, target, index, arr, i+1)
        #notchoosing
        #print(f"Second{i}: subSum = {subSum} subTup = {subTup} tup = {tup} arr = {arr}")
        seq(subSum, subTup, tup, target, index+1, arr, i+1)
        return arr
        
    
def combinationSum(candidates, target):
        arr = []
        return seq(0, (), tuple(candidates), target, 0, arr, 1)

a = [2]
t = 1
print("\n"*100)
print("Start")
print(combinationSum(a, t))
print("Done")
