# -*- coding: utf-8 -*-
'''
一开始就传入 low high 去界定，左右子树根据自身情况
'''
import sys

def valid(root,low,high):
    if root ==None:
        return True
    if root.val <=low or root.val >=high:
        return False
    return valid(root.left,low,root.val) and valid(root.right,root.val,high)

def isValidBST(root):
    return valid(root,-sys.maxint-1,sys.maxint)