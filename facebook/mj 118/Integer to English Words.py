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

print numberToWords(1000)