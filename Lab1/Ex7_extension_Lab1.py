base = 200
Hours = int(input("Enter max hour: "))
step = int(input("Enter step size: ")) 
print(f"{"Hours":>7} | {"Number_of_Bacteria":>12}")
print("-"*30)
for h in range(0, Hours+1, step):
    B=base*(2**h)
    print(f"{h:>5}   | {B:>12}")