# -*- coding: utf-8 -*-

# --------------------skeleton of credit card validator--------------------
card_number = str(input("Enter credit card number you want to check: "))
card_number = '4012888888881881'

# Reverse the credit card number
reversed_card_number = card_number[:: -1]
print(reversed_card_number)

# take the digits in the odd positions and then the digits in the even position
even_numbers = reversed_card_number[1::2]
print(even_numbers)

odd_numbers = reversed_card_number[::2]
print(odd_numbers)

# Add up all the digits in the odd positions into a total.
total = 0
for number in odd_numbers:
    number = int(number)
    total += number
print(total)

# Multiply every even-positioned digit by two;
#   if the product is greater than 9 (e.g. 8 * 2 = 16),
#      then subtract 9 and add the result to the total.
#   Otherwise add the multiplication product to the total.

for number in even_numbers:
    result = int(number) * 2
    if result > 9:
        total += (result - 9)

    else:
        total += result
print(total)

# If the total is divisible by 10 (the remainder after division by 10 is equal to 0 or the number ends in a zero);
#   then the credit card number is valid.

checksum = int(total) % 10

if checksum == 0:
    print("Your credit card is valid")

else:
    print("Your credit card is not valid")
