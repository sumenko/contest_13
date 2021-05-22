class StackMax():
    def __init__(self):
        self.items = []
        self.max_item = None

    def command(self, cmd):
        parsed = cmd.split()
        length = len(parsed)
        if length == 2 and parsed[0] == 'push':
            self.push(int(parsed[1]))

        if length and parsed[0] == 'get_max':
            self.get_max()
        
        if length and parsed[0] == 'pop':
            self.pop()
    
    def pop(self):
        if len(self.items):
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if len(self.items):
            print(max(self.items))
        else:
            print(None)

    def push(self, i):
        self.items.append(i)

            
            


if __name__=='__main__':
    stack = StackMax()

    for i in range(int(input())):
        stack.command(input())