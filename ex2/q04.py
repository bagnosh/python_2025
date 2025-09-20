def allArgs(*args):
    arg_list = []
    for item in args:
        arg_list.append(item)
    return arg_list

print(allArgs(1,2,3,4,"d","c","b","a"))