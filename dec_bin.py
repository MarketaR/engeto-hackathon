import math

output = []
number = int(input("Input number:"))

while number != 0:
    rest = number % 2
    number = math.floor(number / 2)
    output.append(rest)

result = output.reverse()

print(output)

binary = input("Input you binary number:")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print(decimal)
