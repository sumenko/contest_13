# Удаление элемента односвязного списка
# ответ: solution возвращает голову списка с удаленным элементом


class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

# delete
def solution(node, idx) -> Node:
    if idx == 0: 
        return node.next_item
    head = node
    idx-=1
    while idx:
        node = node.next_item
        idx -= 1
    if node.next_item:
        node.next_item = node.next_item.next_item
        return head
    return None

def print_nodes(node) -> None:
    while node:
        print(node.value, end=' ')
        node = node.next_item
    print()

if __name__ == '__main__':
    n = Node('5')
    n1 = Node('4', n)
    n2 = Node('3', n1)
    n3 = Node('2', n2)
    n4 = Node('1', n3)
    n5 = Node('0', n4)

    print_nodes(n5)
    idx = 3
    delete = solution(n5, idx)
    print('idx=', idx)
    print_nodes(delete)