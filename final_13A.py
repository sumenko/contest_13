class Deque():
    def __init__(self, n):
        self.queue_size = n
        self.queue = [None] * n
        self.head = None
        self.tail = None
        self.idx_head = None
        self.idx_tail = None

    def is_empty(self):
        return self.queue_size == 0

    def push_front(x):
        pass

    def push_back(x):
        pass

    def pop_back(self):
        pass

    def pop_front(self):
        pass

    class QueueIsEmpty(Exception):
        pass



tests = (
    ('Test 1',
     """4
4
push_front 861
push_front -819
pop_back
pop_back
""", """861
-819
"""), 
    ('Test 2',
    """7
10
push_front -855
push_front 720
pop_back
pop_back
push_back 844
pop_back
push_back 823
""",
    """-855
720
844
    """
    )
)

def main():

    for name, inp, res in tests:
        print(name, '\n', inp, '\n', res)

if __name__ == '__main__':

    main()