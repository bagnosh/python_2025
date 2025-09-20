import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '**' : operator.pow
}

def operation_table(lst1,lst2,operator):
    if operator not in ops:
        raise ValueError(f"{operator} is not supported. Try a different operator")
    custom_op = lambda x,y: ops[operator](x,y)
    board = []
    board[0].append(operator)
    for i in range(lst2):
        board[0].append(lst2[i])
    for i in range(lst1):
        board[i+1].append(lst1[i])
        for y in lst2:
            board[i+1].append(custom_op(lst1[i],y))
    return board

def table_print(table):
    width = len(table[0])
    length = len(table)
    print('|'.join(str(i) for i in table[0]))
    print('-' * width)
    for i in length-1:
        print('|'.join(str(item) for item in table[i+1]))