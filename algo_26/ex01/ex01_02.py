fib_arr = {0:0, 1:1}
count = 0

def fib_at_n_with_arr(n) :
    global count
    count += 1
    if n <0 :
        return 0
    elif  n in fib_arr :
        return fib_arr[n]
    else :
        new_fib = fib_at_n_with_arr(n-1) + fib_at_n_with_arr(n-2)
        fib_arr[n] = new_fib
        return new_fib
    
print(fib_at_n_with_arr(10))
print("count:" , count) #count: 19
print(fib_at_n_with_arr(20))
print("count:" , count) #count: 40
print(fib_at_n_with_arr(30))
print("count:" , count) #count: 61
print(fib_at_n_with_arr(50))
print("count:" , count) #count: 102
    