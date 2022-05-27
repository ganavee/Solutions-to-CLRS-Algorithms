import sys
class Searching:
    def search(self, string, char):
        for i in string:
            if(i == char):
                return True
        return False
        pass
    
    def input(self):
        print("Enter the String")
        string = sys.stdin.readline().strip()
        print("Enter character to be searched")
        char = sys.stdin.readline().strip()
        print("Input String = {0} and character is {1}".format(string, char))
        print("Is {0} present in {1} ? {2}".format(char, string, self.search(string, char)))
        


obj = Searching()
obj.input()
