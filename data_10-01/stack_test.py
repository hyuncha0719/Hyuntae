
# index 0   1   2   3   4
stack = [None] * 5
top = -1

def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1



def print_stack():
    global top
    print('=== 스택 상태 ===' )
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])
    

# Push 함수
def push(data):
    global top
    top += 1
    stack[top] = data
    return print("현재 top: " + str(top))  

# Pop 함수
def pop():
    global top
    data = stack[top]
    stack[top] = None
    top -= 1
    return print("pop된 데이터 : ", str(data))


# Stack 초기화
init_stack(7)

print_stack()

# push
push('커피')
push('녹차')
push('꿀물')
push('레몬차')

print_stack()

pop()

print_stack()