import pandas as pd

df = pd.DataFrame({"name": ["A", "B", "C", "D", "E", "F"]})

print("Even index:")
print(df[df.index % 2 == 0])

print("Odd index:")
print(df[df.index % 2 == 1])