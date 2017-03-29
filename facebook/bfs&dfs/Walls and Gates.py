# -*- coding: utf-8 -*-
'''
以每个gate为中心开始层次遍历，先把所有gate放到队列中，那么这样就用了 bfs 自带的效果：新访问到的
一定是最短路径，那么以后这个点就不用访问了
'''
def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    m = len(rooms)
    n = 0
    if m != 0:
        n = len(rooms[0])
    map = {}
    que = collections.deque()
    for i in xrange(0, m):
        for j in xrange(0, n):
            if rooms[i][j] == 0:
                que.append((i, j))
                map[(i, j)] = 1
    while len(que) != 0:
        top = que.popleft()
        if top[0] > 0:
            if (top[0] - 1, top[1]) not in map and rooms[top[0] - 1][top[1]] != -1:
                rooms[top[0] - 1][top[1]] = rooms[top[0]][top[1]] + 1
                map[(top[0] - 1, top[1])] = 1
                que.append((top[0] - 1, top[1]))
        if top[0] < m - 1:
            if (top[0] + 1, top[1]) not in map and rooms[top[0] + 1][top[1]] != -1:
                rooms[top[0] + 1][top[1]] = rooms[top[0]][top[1]] + 1
                map[(top[0] + 1, top[1])] = 1
                que.append((top[0] + 1, top[1]))
        if top[1] > 0:
            if (top[0], top[1] - 1) not in map and rooms[top[0]][top[1] - 1] != -1:
                rooms[top[0]][top[1] - 1] = rooms[top[0]][top[1]] + 1
                map[(top[0], top[1] - 1)] = 1
                que.append((top[0], top[1] - 1))
        if top[1] < n - 1:
            if (top[0], top[1] + 1) not in map and rooms[top[0]][top[1] + 1] != -1:
                rooms[top[0]][top[1] + 1] = rooms[top[0]][top[1]] + 1
                map[(top[0], top[1] + 1)] = 1
                que.append((top[0], top[1] + 1))
