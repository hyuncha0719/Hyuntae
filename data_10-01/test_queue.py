def init_queue(size):
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료. 크기: " + str(size))

def enqueue(data):
    global rear
    if is_queue_full():
        return print("큐가 가득 찼습니다.")
    rear += 1
    print_q[rear] = data
    return print("현재 rear : ", str(rear))


def dequeue():
    global front
    if is_queue_empty():
        return print("큐가 비어있습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp

def peek_queue():
    global front
    if is_queue_empty():
        return print("큐가 비어있습니다. peek할 수 없습니다.")
    else :
        temp = print_q[front + 1]
        return temp


def is_queue_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False


def is_queue_full():
    global rear
    if rear == len(print_q) - 1:
        return True
    else:
        return False

def print_queue():
    print('=== 큐 상태 ===')
    for i in range(len(print_q)):
        print(print_q[i])
    print("현재 front : ", str(front))
    print("현재 rear : ", str(rear) )
    print("========================")


init_queue(5)
enqueue('커피')
enqueue('우유')
enqueue('주스')
enqueue('콜라')
enqueue('사이다')

print("================호출전================")
print(peek_queue())
print("================호출후================")
print_queue()




