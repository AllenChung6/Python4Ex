def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


while True:
    x = int(input('Pleas input a number from 0 - 999 \n'))
    print(factorial(x))
