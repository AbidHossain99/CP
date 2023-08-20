'''
Road Construction https://cses.fi/problemset/task/1676
Input:
5 3
1 2
1 3
4 5

Output:
4 2
3 3
2 3
'''

def find_parent(parents, node):
    if parents[node] == node:
        return node
    parents[node] = find_parent(parents, parents[node])
    return parents[node]

def merge_components(parents, sizes, a, b):
    root_a = find_parent(parents, a)
    root_b = find_parent(parents, b)
    if root_a != root_b:
        if sizes[root_a] < sizes[root_b]:
            root_a, root_b = root_b, root_a
        parents[root_b] = root_a
        sizes[root_a] += sizes[root_b]

#input
n, m = map(int, input().split())
parents = list(range(n))
sizes = [1] * n
largest_component_size = 1
component_count = n

def get_largest_component_size(sizes):
    return max(sizes)

for day in range(m):
    a, b = map(int, input().split())

    if find_parent(parents, a - 1) != find_parent(parents, b - 1):
        component_count -= 1
        merge_components(parents, sizes, a - 1, b - 1)
        largest_component_size = max(largest_component_size, get_largest_component_size(sizes))

    print(component_count, largest_component_size)
