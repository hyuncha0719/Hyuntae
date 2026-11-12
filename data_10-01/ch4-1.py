# Node 클래스 정의 i - I - l - L - 0

class Node:
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=', ')
    while current.link != None: # != None = is not None:
        current = current.link
        print(current.data, end=', ')
    print()


memory = []
head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node() # 첫 번쨰 노드 생성
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]: # 두 번째 이후 노드 생성
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)