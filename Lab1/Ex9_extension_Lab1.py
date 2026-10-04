courses = {}

while True:
    name = input("Enter course name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    courses[name] = int(input(f"Enter grade for {name}: "))

if len(courses) == 0:
    print("No courses entered.")
else:
    avg = sum(courses.values()) / len(courses)
    best = max(courses, key=courses.get)
    worst = min(courses, key=courses.get)

    print("Average grade:", round(avg, 2))
    print("Highest grade:", best, courses[best])
    print("Lowest grade:", worst, courses[worst]) 
import os
import pandas as pd

df = pd.DataFrame(list(courses.items()), columns=["course", "grade"])

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "grades.csv")
df.to_csv(path, index=False)
print("Saved to:", path)