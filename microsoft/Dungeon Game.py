def calculateMinimumHP(self, dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m = len(dungeon)
    if m == 0:
        return 0
    n = len(dungeon[0])
    if n == 0:
        return 0
    need = []
    for i in xrange(0, m):
        need.append([0] * n)
    need[m - 1][n - 1] = max(-dungeon[m - 1][n - 1] + 1, 1)
    for i in xrange(m - 2, -1, -1):
        need[i][n - 1] = max(1, need[i + 1][n - 1] - dungeon[i][n - 1])
    for i in xrange(n - 2, -1, -1):
        need[m - 1][i] = max(1, need[m - 1][i + 1] - dungeon[m - 1][i])
    for i in xrange(m - 2, -1, -1):
        for j in xrange(n - 2, -1, -1):
            need[i][j] = min(need[i + 1][j], need[i][j + 1]) - dungeon[i][j]
            need[i][j] = max(need[i][j], 1)
    return need[0][0]