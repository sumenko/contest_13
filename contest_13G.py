# import time

class StackMax():
    def __init__(self):
        self.items = []
        self.max_items = []

    def get_max(self):
        if self.items != []:
            print(max(self.items))
        else:
            print('None')

    def pop(self):
        try:
            item = self.items.pop()
        except IndexError:
            print('error')
            return

    def push(self, i):
        self.items.append(i)
        
        if self.max_items == []:
            self.max_items.append(i)
        
        if i > self.max_items[-1]:
            self.max_items.append(i)


def main():
    stack = StackMax()
    
    
    n = int(input())
    for i in range(n):
        command = input()

        if 'get_max' in command:
            stack.get_max()
        elif 'pop' in command:
            stack.pop()
        elif 'push' in command:
            stack.push(int(command.rstrip().split()[1]))



if __name__=='__main__':
    main()