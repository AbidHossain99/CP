'''
Forest Queries https://cses.fi/problemset/task/1652
Input:
4 3
.*..
*.**
**..
****
2 2 3 4
3 1 3 1
1 1 2 2

Output:
3
1
2
'''


def count_trees_in_rectangle(forest, y1, x1, y2, x2):
    count = 0
    for i in range(y1 - 1, y2):
        for j in range(x1 - 1, x2):
            if forest[i][j] == '*':
                count += 1
    return count

#input
n, q = map(int, input().split())
forest = [input() for _ in range(n)]

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    result = count_trees_in_rectangle(forest, y1, x1, y2, x2)
    print(result)
