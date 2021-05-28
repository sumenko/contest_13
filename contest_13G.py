class StackMax():
    def __init__(self):
        self.items = []
        self.max_items = []

    def get_max(self):
        if self.items != []:
            print(self.max_items[-1])
        else:
            print('None')

    def pop(self):
        try:
            item = self.items.pop()
        except IndexError:
            self.max_items = []
            print('error')
            return

        if item == self.max_items[-1]:
            self.max_items.pop()

    def push(self, num):
        self.items.append(num)
        
        if self.max_items == [] or num >= self.max_items[-1]:
            self.max_items.append(num)

def main():
    stack = StackMax()
    
    n = int(input())
    for _ in range(n):
        command = input()

        if 'get_max' in command:
            stack.get_max()
        elif 'pop' in command:
            stack.pop()
        elif 'push' in command:
            stack.push(int(command.rstrip().split()[1]))

def run_file(fname, silent=False):
    """ Для ручной отладки """
    stack = StackMax()

    with open(fname, 'r') as inp:
        n = int(inp.readline())
        for _ in range(n):
            command = inp.readline().split('\n')[0]
            if not silent: print('>>>', command)
            if 'get_max' in command:
                stack.get_max()
            elif 'pop' in command:
                stack.pop()
            elif 'push' in command:
                stack.push(int(command.rstrip().split()[1]))

if __name__=='__main__':
    main()
