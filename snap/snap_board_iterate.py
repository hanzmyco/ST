import copy
def dfs(board,m,dic,times,i,j,output,box):
    num=dic[(i,j)]
    if num < m:
        output.append(board[i][j])
        dic[(i,j)]+=1
        leng = len(board)

        if num==0:

            if i>0:
                dfs(board,m,dic,times+1,i-1,j,output,box)
            if i<leng-1:
                dfs(board,m,dic,times+1,i+1,j,output,box)
            if j >0:
                dfs(board,m,dic,times+1,i,j-1,output,box)
            if j <leng-1:
                dfs(board, m, dic, times+1, i, j + 1, output, box)
            times+=1
        else:
            if i > 0:
                dfs(board, m, dic, times , i - 1, j, output, box)
            if i < leng - 1:
                dfs(board, m, dic, times , i + 1, j, output, box)
            if j > 0:
                dfs(board, m, dic, times , i, j - 1, output, box)
            if j < leng - 1:
                dfs(board, m, dic, times , i, j + 1, output, box)
        if times == leng * leng:
            box.append(copy.deepcopy(output))

        output.pop()
        dic[(i,j)]-=1

board=[[1,2],[3,4]]
m=2
output=[]
box=[]
n=len(board)
dic={}
for i in xrange(0,n):
    for j in xrange(0,n):
        dic[(i,j)]=0
dfs(board,m,dic,0,0,0,output,box)
print len(box)
print box



