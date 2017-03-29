4.中国小哥，非常nice， 一直follow我的思路。 1.input friends relation {{1，2}， {2，3}， {3，4}} 把用户存在两个group里， 每个group里大家都不互相认识。所以exp应该g1{1，3} g2{2，4}。
其他情况和小哥讨论一下，我自己想如何设计都可以，比如所有人都不认。 很快写完，最后考虑corner case的时候，小哥提醒了一下。

anser : 先sort，然后两层循环，每次循环把（x,y) 分到两组（x,y里要么肯定有一个已经被分好了，要么就和前面的都毫不相干），然后对剩下的含有x，y的分组，然后再

2.input 是array {1，2，3，0，4}。到达最后一个格子最短步数，每个数字代表最多可以跳几下。应该是lc的题吧，忘记了。不过很快dp秒掉。 后来，小哥就把我送了出来。。。

dp=[int-max]*n
for i in xrange(0,n-1):
    for j in xrange (i+1,min(,i+a[i]+1,n):
        dp[j]=min(dp[j],dp[i]+1)
