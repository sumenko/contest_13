class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

# delete
def solution(node, idx) -> Node:
    pass
    # while node:
    #     print(node.value)
    #     node = node.next_item




n = Node('16')
n1 = Node('sdfsf', n)
n2 = Node('aaaa1', n1)
n3 = Node('aaaa2', n2)
n4 = Node('aaaa3', n3)
n5 = Node('aaaa4', n4)

solution(n5)