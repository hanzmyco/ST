# -*- coding: utf-8 -*-
'''
每次处理三位, map1存【'',one，two,ninteen], map2存【""，""，twenty,thirty, ninty]
对于一个3位数，a=num/100,看看有几百，b=num%100, c%10, c管个位
如果b<20，那么res=map1[b], 否则res=map2[b/10],如果c！=0,res+=' '+ map1[c]
如果a>0, res1=map1[a]+' '+hundred, b!=0就 return res1 + ' ' +res
否则return res1

如果a==0；return res
每次处理3位，先处理个十百，然后/1000, 放进去看看

'''




def converHundred(num):
    map1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    map2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    a = num / 100
    b = num % 100
    c = num % 10
    if b < 20:
        res = map1[b]
    else:
        res = map2[b / 10]
        if c != 0:
            res = res + ' ' + map1[c]
    if a > 0:
        res1 = map1[a] + ' ' + 'Hundred'
        if b != 0:
            return res1 + ' ' + res
        else:
            return res1
    return res


def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    res = converHundred(num % 1000)  # get 3 digits
    map_3 = ["Thousand", "Million", "Billion"]
    for i in xrange(0, 3):
        num = num / 1000
        if num % 1000 != 0:
            res = converHundred(num % 1000) + ' ' + map_3[i] + ' ' + res
    l = len(res)
    while l != 0 and res[l - 1] == ' ':
        l -= 1
    if len(res) == 0:
        return 'Zero'
    return res[:l]

print numberToWords(1257680)