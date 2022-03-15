def fibonnaci(n):
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

while True:
    n = int(input("Please pick a number from 0 - 30 \n"))
    print(fibonnaci(n))
