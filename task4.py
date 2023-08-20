'''
Tree Distances I https://cses.fi/problemset/task/1132
Input:
5
1 2
1 3
3 4
3 5

Output:
2 3 2 3 3
'''
def bfs(node, graph, n):
    visited = [False] * (n + 1)
    max_distance = 0

    queue = []
    queue.append((node, 0))  
    visited[node] = True

    while queue:
        current_node, depth = queue.pop(0)
        max_distance = depth

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                queue.append((neighbor, depth + 1))
                visited[neighbor] = True

    return max_distance

#input
n = int(input())
graph = [[] for _ in range(n + 1)]  

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

max_distances = [0] * (n + 1)

for i in range(1, n + 1):
    max_distances[i] = bfs(i, graph, n)

for i in range(1, n + 1):
    print(max_distances[i], end=" ")
