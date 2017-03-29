# -*- coding: utf-8 -*-
'''
每次保证all[start%length]在空格之后的下一个字母上

'''
def wordsTyping1(sentence,rows,cols):
    all=''
    for word in sentence:
        all+=word+' '
    start,leng=0,len(all)
    for i in xrange(0,rows):
        start+=cols
        if all[start%leng]==' ':
            start+=1
        else:
            while start >0 and all[(start-1)%leng]!=' ':
                start-=1
    return start / leng

print wordsTyping1(['hello','world'],2,8)
print wordsTyping1(['a','bcd','e'],3,6)
print wordsTyping1(["I", "had", "apple", "pie"],4,5)