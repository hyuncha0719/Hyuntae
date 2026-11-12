class Node:
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current == None:
        return
    while current != None:
        print(current.data, end=' ')
        current = current.link
    print()

def insert_node(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data: # 첫 번째 노드 앞에 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node

    print_nodes(head)


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

    insert_node("다현", "재남")
    print_nodes(head)
    insert_node("사나", "솔라")
    print_nodes(head)
    insert_node("재남", "문별")
    print_nodes(head)
