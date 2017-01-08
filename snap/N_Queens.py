class Solution(object):
    def search(self, results, cols, n):
        if len(cols) == n:
            results.append(self.drawChess(cols))
        for colIndex in xrange(0, n):
            if self.isValid(cols, colIndex) == False:
                continue
            cols.append(colIndex)
            self.search(results, cols, n)
            cols.pop(len(cols) - 1)

    def isValid(self, cols, colIndex):
        for index, ite in enumerate(cols):
            if colIndex == ite:
                return False
            if abs(colIndex - ite) == abs(index - len(cols)):
                return False
        return True

    def drawChess(self, cols):
        output = []
        for ite in cols:
            row = '.' * ite + 'Q' + '.' * (len(cols) - ite - 1)
            output.append(row)
        return output

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return []
        results = []
        cols = []
        self.search(results, cols, n)
        return results