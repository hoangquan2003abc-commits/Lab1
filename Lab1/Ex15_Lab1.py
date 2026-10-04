n = int(input("Enter a three-digit integer: "))
while n<100 or n>999: 
    print(f"{n} is not a three-digit integer,please enter a three-digit integer")
    n = int(input("Enter a three-digit integer: "))

hundreds = n // 100
tens = (n // 10) % 10
units = n % 10

total = hundreds + tens + units
reversed_n = units * 100 + tens * 10 + hundreds

print("Hundreds:", hundreds)
print("Tens:", tens)
print("Units:", units)
print("Sum of digits:", total)
print("Reversed number:", reversed_n)

if n == reversed_n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")