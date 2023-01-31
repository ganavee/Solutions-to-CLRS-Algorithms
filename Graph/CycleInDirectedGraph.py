class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        #print("adj = ", adj)
        visited = [None]*V
        path = [None]*V
        for i in range(len(visited)):
            if(visited[i] == None):
                stack = []
                stack.append(i)
                if(self.dfs(i, path, visited, adj) == True):
                    return True
        return False
        # code here
        
        
    def dfs(self, node, path, visited, adj):
        if(visited[node] == 1):
            if(path[node] == 1):
                return True
            else:
                return False
        visited[node] = 1
        path[node] = 1
        x = 0
        result = False
        for i in adj[node]:
            x = 1
            result1 = self.dfs(i, path, visited, adj)
            result = result or result1
        path[node] = 0
        return result

adj = [[], [2], [3], [4, 7], [5], [6], [], [5], [2, 9], [10], [8]]
obj = Solution()
print("Cycle? ", obj.isCyclic(11, adj))
