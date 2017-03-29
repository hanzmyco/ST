class min_sweeper(object):
    def __init__(self, arr):
        self.arr=arr
        self.len=len(arr)
        self.front_end=['*']*self.len
    def left_click(self, index):
        num=0
        if self.arr[index]==1:
            return False
        if index ==0 or index<self.len-1:

            if self.arr[index + 1] == 1:
                num += 1
        if index == self.len-1 or index >0:
            if self.arr[index - 1] == 1:
                num += 1
        self.front_end[index] = str(num)
        if num==0:
            if index>0 and self.front_end[index-1]=='*':
                self.left_click(index-1)
            if index<self.len-1 and self.front_end[index+1]=='*':
                self.left_click(index+1)
    def left_check(self,index,direction):
        if direction ==1: # from right
            if index>0:
                if self.arr[index-1] ==1:
                    self.front_end[index]=1
                else:
                    self.front_end[index]=0
                    if index==1:
                        self.front_end[index-1]=0
                    else:
                        self.left_check(index-1,1)
            else:
                self.front_end[index]=0
        # same for direction from left



arr=[0,1,0,0,0,1,0]
ms=min_sweeper(arr)
ms.left_click(3)
print ms.arr
print ms.front_end






