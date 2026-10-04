import pandas as pd

base = 200
max_hour = int(input("Enter max hour: "))
step = int(input("Enter step size: "))

hour_list = list(range(0, max_hour + 1, step))
bacteria = [base * (2 ** h) for h in hour_list]

df = pd.DataFrame({"Hour": hour_list, "Number of Bacteria": bacteria})

df.to_csv("bacteria.csv", index=False)
df.to_excel("bacteria.xlsx", index=False) 
import os

print("Saved to:", os.path.abspath("bacteria.csv"))