import sys

class Graph:
    def __init__(self):
        self.adj = None
        self.vertices = 0
        self.visited = []
        self.dfs = []

    def depth_first_search(self):
        stack = []
        for i in range(self.vertices):
            if(self.visited[i] == 0):
                print("DFS of component ", self.dfs)
                self.dfs = []
                stack.append(i)
            else:
                continue
            while(len(stack)):
                popped = stack.pop()
                if(self.visited[popped] == 0):
                    self.dfs.append(popped)
                    self.visited[popped] = 1
                    for i in self.adj[popped]:
                        if i != None:
                            stack.append(i)
        print("DFS of component ", self.dfs)
        
    def read_input(self):
        input = sys.stdin.readline()
        input = list(map(int, input.strip().split()))
        self.vertices, tot_edges = input[:2]
        self.visited = [0 for i in range(self.vertices)]
        input = input[2:]
        edges = list(zip(input[0::2], input[1::2]))
        self.adj = [[] for i in range(self.vertices)]
        for(u, v) in edges:
            self.adj[u-1].append(v-1)
            self.adj[v-1].append(u-1)
        print("Adjacency list ", self.adj)


obj = Graph()
obj.read_input()
obj.depth_first_search()
