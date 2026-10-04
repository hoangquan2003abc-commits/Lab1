def name_score(name):
    return sum(ord(c) for c in name)
def winner(name_list):
    return max(name_list, key=name_score)
names = input("Enter names separated by commas: ").split(",")
names = [n.strip() for n in names] 
for n in names:
    print(n, "score", name_score(n))
print(winner(names),"go first!")