import sys

class inputs:
    def input(self):
    #using input
        x = input("Please enter input ")
        print("Input is ", x)

    def input_readline(self):
        #4 2 3 2 1 4
    #using readline
        print("Enter input")
        x = sys.stdin.readline()
        print("Input is {0}type is {1}".format(x, type(x)))
        x = list(map(int, x.strip().split()))
        print("After list ", x)
        print(x[:2])
        n, m = x[:2]
        print("n = {0} m = {1} type of n {2}".format(n, m, type(n)))
        x = x[2:]
        print("remaining numbers ", x)
        print("1 ", x[0::2])
        print("2 ", x[1::2])
        


obj = inputs()
obj.input_readline()
