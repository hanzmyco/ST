# -*- coding: utf-8 -*-
'''
先用minheap存k个，然后每次如果比最小的大，就替换掉，heapify，最后把heap【0】返回就是第K大的了


'''

'''
Method 3 (Using Max-Heap)
We can also use Max Heap for finding the k’th smallest element. Following is algorithm.
1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

2) For each element, after the k’th element (arr[k] to arr[n-1]), compare it with root of MH.
……a) If the element is less than the root then make it root and call heapify for MH
……b) Else ignore it.
// The step 2 is O((n-k)*logk)

3) Finally, root of the MH is the kth smallest element.

Time complexity of this solution is O(k + (n-k)*Logk)

'''
