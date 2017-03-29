# -*- coding: utf-8 -*-
'''

所有0如果全被2包住，那么不会被遍历到，如果唯一出路是1，那么除了在它旁边的一开始遍历的时候，并且是第一次，它能被访问到，其他都不会，因为默认
是要能访问所有的1

'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid[0]) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        distance = []
        buildingNum = 0
        summ = []
        for i in xrange(0, row):
            distance.append([0] * col)
            summ.append([0] * col)

        color_need = 0
        res = 10000
        for i in xrange(0, row):
            for j in xrange(0, col):
                if grid[i][j] == 1:
                    buildingNum += 1
                    que = collections.deque()
                    que.append((i, j))
                    res = 10000
                    distance[i][j] = 1
                    while len(que) != 0:
                        q_size = len(que)
                        for number in xrange(0, q_size):
                            x, y = que.popleft()
                            if x > 0 and grid[x - 1][y] == color_need:
                                distance[x - 1][y] = distance[x][y] + 1
                                grid[x - 1][y] -= 1
                                que.append((x - 1, y))
                                summ[x - 1][y] += distance[x - 1][y] - 1
                                res = min(res, summ[x - 1][y])
                            if x < row - 1 and grid[x + 1][y] == color_need:
                                distance[x + 1][y] = distance[x][y] + 1
                                grid[x + 1][y] -= 1
                                que.append((x + 1, y))
                                summ[x + 1][y] += distance[x + 1][y] - 1
                                res = min(res, summ[x + 1][y])

                            if y > 0 and grid[x][y - 1] == color_need:
                                distance[x][y - 1] = distance[x][y] + 1
                                grid[x][y - 1] -= 1
                                que.append((x, y - 1))
                                summ[x][y - 1] += distance[x][y - 1] - 1
                                res = min(res, summ[x][y - 1])
                            if y < col - 1 and grid[x][y + 1] == color_need:
                                distance[x][y + 1] = distance[x][y] + 1
                                grid[x][y + 1] -= 1
                                que.append((x, y + 1))
                                summ[x][y + 1] += distance[x][y + 1] - 1
                                res = min(res, summ[x][y + 1])

                    color_need -= 1
        if res == 10000:
            return -1
        return res