def fibonacci(n):
    a = 0
    b = 1
    print(a, b, " ")
    while n - 1:
        c = a + b
        a, b = b, c
        print(c, " ")
        n = n - 1


print(fibonacci(7))
