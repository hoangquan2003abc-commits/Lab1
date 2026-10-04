import matplotlib.pyplot as plt

o = float(input("Enter original hourly wage: "))
p = float(input("Enter percentage change per year (e.g. 3 or -3): ")) / 100
n = int(input("Enter number of years: "))

w = o * (1 + p) ** n
print("Final wage:", round(w, 2))

reviews = input("Enter reviews separated by commas (good/bad): ").split(",")
reviews = [r.strip().lower() for r in reviews]
while len(reviews) != n:
    print(f"You must enter exactly {n} reviews (you entered {len(reviews)}).")
    reviews = input("Enter reviews separated by commas (good/bad): ").split(",")
    reviews = [r.strip().lower() for r in reviews]
wages = [o]
for r in reviews:
    if r == "good":
        wages.append(wages[-1] * 1.03)
    elif r == "bad":
        wages.append(wages[-1] * 0.97)
    else:
        print("Unknown review:", r, "(skipped)")

print("Final wage after reviews:", round(wages[-1], 2))

years = list(range(len(wages)))

plt.plot(years, wages, marker="o")
plt.xlabel("Year")
plt.ylabel("Hourly wage ($)")
plt.title("Wage by year")
plt.grid(True)
plt.show()