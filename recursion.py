def factorial(num):
    if num == 0:
        return 1
    else:
        return (factorial(num - 1) * num)

print(factorial(5))


def fibonacci(num):
    number = 0
    if num == 0:
        number = 0
    elif num == 1:
        number = 1
    else:
        number = int((fibonacci(num - 2) + fibonacci(num - 1)))
    print(str(number))
    return number

fibonacci(4)


def GCD(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r

    result = num1
    print(result)

GCD(15, 20)
