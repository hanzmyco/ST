def add_combo(combo):
    output=[]
    if len(combo)!=0:
        for ite in combo[0]:
            out1=add_combo(combo[1:])
            if out1!=[]:
                for ite1 in out1:
                    output.append(ite + ite1 )
            else:
                output.append(ite)
    return output



def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    wrong_po = []
    stack = []
    num_left = 0
    begins = []
    begin = 0
    combo = []
    last=0
    for i in xrange(0, len(s)):
        if s[i] == '(':
            # stack.append((i,0))
            if num_left >= 0:
                num_left += 1
            else:
                num_left = 1
        elif s[i] == ')':
            if num_left > 0:
                num_left -= 1
                # stack.pop()
                stack.append(i)  # add right prenthies index

            elif num_left == 0:
                if len(stack)!=0:

                        com = []
                        for index in stack:
                            st = s[begin:index] + s[index + 1:i + 1]
                            com.append(st)
                        begin = i + 1
                        num_left -= 1
                        combo.append(com)
                        last=i+1
                        stack=[]
            else:
                        last+=1
                        begin+=1
    tail=''
    if last>0:
        tail=s[last:]
    print combo
    out=add_combo(combo)
    print out
    print tail

s='()())()()())()'
s='()'
removeInvalidParentheses(s)
