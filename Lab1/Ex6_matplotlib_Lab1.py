import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
base = 200
max_hour = int(input("Enter max hour: "))
step = int(input("Enter step size: "))
hours = list(range(0, max_hour + 1, step))
bacteria = [base * (2 ** h) for h in hours]
plt.plot(hours, bacteria, marker="o")
plt.xlabel("Hour")
plt.ylabel("Number of Bacteria(thousands)")
plt.title("Bacteria Growth")
plt.grid(True)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{x/1000:,.0f}")) 
plt.show()