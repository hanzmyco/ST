s1='3+2*2'
s2='3/2'
s3=" 3+5 / 2 "

def calculator(s):
    op_stack = []
    num_stack = []
    dic = {}
    dic['+'] = 0
    dic['-'] = 0
    dic['*'] = 0
    dic['/'] = 0
    index=len(s)-1
    while index>=0:
        ite=s[index]

        if ite in dic:
            if len(op_stack) == 0:
                op_stack.append(ite)
            else:
                    if op_stack[0] == '+' or op_stack[0] == '-':
                        op_stack.insert(0, ite)
                    else:
                        if ite == '+' or ite =='-':
                            left = num_stack.pop(0)
                            right = num_stack.pop(0)
                            op=op_stack.pop(0)
                            if op=='*':
                                num_stack.insert(0, left * right)
                            else:
                                num_stack.insert(0, left / right)


                        op_stack.insert(0, ite)

        elif ite != ' ':
            num_stack.insert(0, int(ite))

        index-=1
    op=op_stack[0]
    #print op_stack
    #print num_stack
    if op == '+':
        left = num_stack.pop(0)
        right = num_stack.pop(0)
        print left + right
    elif op == '-':
        left = num_stack.pop(0)
        right = num_stack.pop(0)
        print  left - right
    elif op =='*':
        left = num_stack.pop(0)
        right = num_stack.pop(0)
        print  left * right
    else:
        left = num_stack.pop(0)
        right = num_stack.pop(0)
        print  left / right



calculator(s1)
calculator(s2)
calculator(s3)