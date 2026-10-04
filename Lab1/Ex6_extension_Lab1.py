base = 200
max_hour = int(input("Enter max hour: "))
step = int(input("Enter step size: "))
print("Hours\tNumber of Bacteria")
for h in range(0, max_hour+1, step):
    B=base*(2**h)
    print(f"{h}\t{B}")