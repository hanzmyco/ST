# -*- coding: utf-8 -*-
'''
几何判断

'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m != 0:
            n = len(matrix[0])
        else:
            return
        self.f = [[matrix[0][0]]]
        for i in xrange(1, n):
            self.f[0].append(self.f[0][i - 1] + matrix[0][i])
        for j in xrange(1, m):
            self.f.append([self.f[j - 1][0] + matrix[j][0]])
        for i in xrange(1, m):
            for j in xrange(1, n):
                self.f[i].append(self.f[i - 1][j] + self.f[i][j - 1] - self.f[i - 1][j - 1]+matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > 0 and col1 > 0:
            return self.f[row2][col2] + self.f[row1 - 1][col1 - 1] - self.f[row1 - 1][col2] - self.f[row2][col1 - 1]
        elif row1 == 0 and col1 != 0:
            return self.f[row2][col2] - self.f[row2][col1 - 1]
        elif row1 != 0 and col1 == 0:
            return self.f[row2][col2] - self.f[row1 - 1][col2]
        else:
            return self.f[row2][col2]

matrix=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
nm=NumMatrix(matrix)
print nm.f
print nm.sumRegion(2,1,4,3)