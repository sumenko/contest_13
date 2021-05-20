# Поиск элемента односвязного списка по значению
# ответ: solution возвращает индекс найденного элемента или -1 если не найден


class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def solution(node, elem) -> int:
    idx = 0
    while node:
        if node.value == elem: return idx
        node = node.next_item
        idx += 1
    return -1

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
    search = '5'
    print(f'search for: {search} idx=', solution(n5, search))
    search = '0'
    print(f'search for: {search} idx=', solution(n5, search))
    search = '11'
    print(f'search for: {search} idx=', solution(n5, search))
