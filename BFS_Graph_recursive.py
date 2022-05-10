import sys

class Graph:
    def __init__(self):
        self.adj = None
        self.vertices = 0
        self.visited = []
        self.bfs = []
        self.queue = []

    def bfs_algo(self):
        if(len(self.queue)):
            popped = self.queue.pop(0)
            if(self.visited[popped] == 0):
                self.visited[popped] = 1
                self.bfs.append(popped)
                for i in self.adj[popped]:
                    if i is not None:
                        self.queue.append(i)
                self.bfs_algo()
            else:
                self.bfs_algo()
        else:
            return

    def recursive_breadth_first_search(self):
        for i in range(self.vertices):
            if(self.visited[i] == 0):
                self.queue.append(i)
                self.bfs_algo()
                print("BFS of the component Graph ", self.bfs)
                self.bfs = []
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
obj.recursive_breadth_first_search()
