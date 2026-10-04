numbers=list(map(int,input("Input numbers between 1 to 10:").split()))
for number in numbers:
 if 1<=number<=10:
  print("the square of", number, "is", number**2)
 else:
  print(number,"is out of range")