# Разворот двусвязного списка
# ответ: solution возвращает голову развёрнутого списка


class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    while node.next:
        node = node.next
    head = node
    while node:
        prev_temp = node.prev
        node.prev = node.next
        node.next = prev_temp
        node = prev_temp
    
    return head

def print_dnodes(node):
    while node:
        print(node.value, end=' > ')
        node = node.next
    print()


if __name__ == '__main__':
    dnode0 = DoubleConnectedNode('3', next = None, prev = None)
    dnode1 = DoubleConnectedNode('2', next = None, prev = dnode0)
    dnode2 = DoubleConnectedNode('1', next = None, prev = dnode1)
    dnode0.next = dnode1
    dnode1.next = dnode2

    print_dnodes(dnode0)
    print('<- reversed ->')
    print_dnodes(solution(dnode0))
    