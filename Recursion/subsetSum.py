class Solution:
    def seq(self, subSum, subTup, tup, index, result, i):
        #print(f"subSum = {subSum} subTup = {subTup}, index = {index}, result = {result}")
        
        if(index < 0):
            result.append(subSum)
            return result
        newSubTup = subTup + (tup[index],)
        #print(f"First{i}: subSum = {subSum+ tup[index]} newSubTup = {newSubTup}, index = {index}, result = {result}")
        self.seq(subSum + tup[index], newSubTup, tup, index-1, result, i+1)
        #print(f"Second{i}: subSum = {subSum} subTup = {subTup}, index = {index}, result = {result}")
        self.seq(subSum , subTup, tup, index-1, result, i+1)
        return result
    
    def subsetSums(self, arr, N):
        result = []
        return list(sorted(self.seq(0, (), tuple(arr), N-1, result, 0)))

a = [2, 5, 8, 11, 13]
obj = Solution()
print(obj.subsetSums(a, len(a)))
