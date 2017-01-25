from collections import deque

def cal_m(s):
  a=0
  b=0
  map={'(':1,')':-1}
  for ite in s:
    a+=map.get(ite,0)
    b+=a<0
    a=max(a,0)
  return a+b

def bfs1(s):
    output=[]
    mistake=cal_m(s)
    if mistake==0:
        return [s]
    filter=set()
    que=deque()
    que.append(s)
    dic={}
    dic[s]=1
    while len(que)>0:
        top=que.popleft()
        for i in xrange(0,len(top)):
            if top[i]!='(' and top[i]!=')':
                continue
            new_s=top[:i]+top[i+1:]
            if new_s in dic:
                continue
            mistake_new=cal_m(new_s)
            dic[new_s]=1
            if mistake_new==0:
                output.append(new_s)
            elif mistake_new <= mistake:
                que.append(new_s)
                mistake=mistake_new

    print output

test='(((k()(('
bfs1(test)