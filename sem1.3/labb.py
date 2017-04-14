def fib(n):
    a, b = 1, 1
    step = 0
    while step < n:
        yield b
        b, a = a + b, b
        step += 1

def fibr(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibr(n - 1) + fibr(n - 2)

for i in fib(5):
    print(i)

for i in range(5):
    print (fibr(i))