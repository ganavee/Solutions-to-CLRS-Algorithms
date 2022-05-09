import sys

class inputs:
    def input(self):
    #using input
        x = input("Please enter input ")
        print("Input is ", x)

    def input_readline(self):
        #4 2 3 2 1 4
    #using readline
        input = sys.stdin.readline()
        print("input from console ", input)
        input = list(map(int, input.strip().split()))
        print("input from modification ", input)
        vertices, tot_edges = input[:2]
        print("Number of veritces {0} \nNumber of edges {1}".format(vertices, tot_edges))
        input = input[2:]
        print("input from trimming ", input)
        edges = list(zip(input[0:-2:2], input[1:-2:2]))
        print("edges list ", edges)
        adj = [[] for i in range(vertices)]
        for (u,v) in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        print("Adjacency list ",adj)


obj = inputs()
obj.input_readline()
