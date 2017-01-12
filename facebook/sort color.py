def sort_colors(a):
    pl=0
    pr=len(a)-1
    i=0
    while i<=pr:
        if a[i]==0:
            swap(a,pl,i)
            pl+=1
            i+=1
        elif a[i]==1:
            i+=1
        else:
            swap(a,pr,i)
            pr-=1
def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
