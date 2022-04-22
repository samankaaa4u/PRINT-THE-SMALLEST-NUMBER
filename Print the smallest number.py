import random

class Find_Smallest_Number:
    def execution(self):
        self.smallest = 1234567890
    
        self.my_list = []

        for self.i in range(10):
            self.my_list = random.randrange(0,1000)
            print(self.my_list)

            self.smallest = min(self.my_list, self.smallest)
        print()
        print('The Smallest Number is:')
        return self.smallest

test = Find_Smallest_Number()
result = test.execution()
print(result)
