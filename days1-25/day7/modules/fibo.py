def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, b+a
    return result

fib_nums = [0,1,1,2,3,5,8,13,21,34,55]