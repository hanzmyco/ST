def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        dic={}
        n=len(matrix)
        visited={}
        for i in xrange(0,n):
            for j in xrange(0,n):
                dic[(i,j)]=matrix[i][j]
                visited[(i,j)]=0
        visited[dic[0,0]]=1
        heap=[]
        heap[0]=(0,0,dic[(0,0)])
        dx=(0,1)
        dy=(1,0)
        for i in xrange(0,k-1):
            cur=heapq.heappop(heap)
            for j in xrange(0,2):
                next_x=cur[0]+dx[j]
                next_y=cur[1]+dy[j]
                if next_x<n and next_y<n and visited[(next_x,next_y)]==0:
                    visited[(next_x,next_y)]=1
                    heapq.push((next_x,next_y,dic[(next_x,next_y)]))
        return min(heap)[2]
