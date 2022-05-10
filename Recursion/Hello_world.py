class Recursion:

    #To print Hello world a number of times
    def message(self, current_count, total_count):
        if(current_count < total_count):
            print("Hello world")
            self.message(current_count+1, total_count)
            #print("Coming back current_count = ", current_count)

    #To print numbers till a particular value
    def numbers(self, start_value, end_value):
        if(start_value <= end_value):
            print(start_value)
            self.numbers(start_value+1, end_value)

obj = Recursion()
obj.message(0, 5)
obj.numbers(0,5)
