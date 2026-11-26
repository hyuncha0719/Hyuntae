class graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]



def print_graph(graph):
    print("===" + graph + "그래프 정보 출력 ===")
    for row in range(graph.SIZE):
        for col in range(graph.SIZE):
            print(graph.graph[row][col], end=' ')
        print()


# 전역 번수 선언부
GI, G3 =None, None


GI = graph(4)
GI.graph[0][1] = 1
GI.graph[0][2] = 1
GI.graph[0][3] = 1
GI.graph[1][0] = 1
GI.graph[1][2] = 1
GI.graph[2][0] = 1
GI.graph[2][1] = 1
GI.graph[2][3] = 1
GI.graph[3][0] = 1
GI.graph[3][2] = 1
print_graph(GI)


G3 = graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1

print("=== G3 부정형 그래프 ===")
for row in range(G3.SIZE):
    for col in range(G3.SIZE):
        print(G3.graph[row][col], end=' ')
    print()
