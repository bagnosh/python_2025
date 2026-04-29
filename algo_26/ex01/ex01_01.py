count = 0

def fib_at_n(n):
    global count
    count += 1
    if n <= 1:
        return n
    else:
        return fib_at_n(n-1) + fib_at_n(n-2)


print(fib_at_n(10)) #55
print("count:" , count) #count: 177
print(fib_at_n(20)) #6765
print("count:" , count) #count: 22068
print(fib_at_n(30)) #832040
print("count:" , count) #count: 2714605
print(fib_at_n(50)) #12586269025
print("count:" , count) #count: 40732736752 (terminal froze for more than an hour)