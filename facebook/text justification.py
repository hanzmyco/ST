def fullJustify(words, maxWidth):
    res=[]
    begin_index=0
    L=maxWidth

    while begin_index < len(words):
        end_index=begin_index # end_index  is the next index of the end index of each line
        l=0     # len is the total number of text(no space), each line
        while end_index<len(words) and l+len(words[end_index])+end_index-begin_index <=L:
            l+=len(words[end_index])
            end_index+=1
        text=''
        space = L - l  # how many space we have left for the remaining text in this line
        for k in xrange(begin_index,end_index): # k iterate through each word in the line
            text+=words[k]
            if space >0:
                each_space=0
                if end_index == len(words): # already the last line we need
                    if end_index-k==1 : # k is the last word
                        each_space=space
                    else:
                        each_space =1 # in the last line, every word except the last one has one space
                else:
                    if end_index- k -1>0: # not the last word in this line
                        if space % (end_index-k-1)==0: # remaing word is dividible
                            each_space=space/(end_index-k-1)
                        else:
                            each_space=space / (end_index-k-1) +1
                    else: #last word in a line (not last line)
                        each_space=space # the remaining space
                text+=' '*each_space
                space-=each_space
        res.append(text)
        begin_index=end_index

    return res

words=["This", "is", "an", "example", "of", "text", "justification."]
words=['']
print fullJustify(words,16)