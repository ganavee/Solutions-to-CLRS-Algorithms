import sys

class Graph:
    def __init__(self):
        self.adj = None
        self.vertices = 0
        self.visited = []
        self.dfs = []
        self.queue = []

    def dfs_algo(self):
        #print("Entering dfs_algo lenght = ", len(self.queue))
        if(len(self.queue) != 0):
            popped = self.queue.pop()
            #print("After popping ", self.queue)
            if(self.visited[popped] == 0):
                self.visited[popped] = 1
                self.dfs.append(popped)
                for i in self.adj[popped]:
                    if i is not None:
                        self.queue.append(i)
                #print("Queue = {0} DFS = {1} len{2}".format(self.queue, self.dfs, len(self.queue)))
                self.dfs_algo()
            else:
                self.dfs_algo()
        else:
            return

    def recursive_depth_first_search(self):
        for i in range(self.vertices):
            if(self.visited[i] == 0):
                self.queue.append(i)
                self.dfs_algo()
                print("DFS for single component Graph ", self.dfs)
                self.dfs = []
            else:
                continue
            
                
        
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
obj.recursive_depth_first_search()
