a = float(input('Enter time for runner 1: '))
b = float(input('Enter time for runner 2: '))
c = float(input('Enter time for runner 3: '))

runners = [(a, 1), (b, 2), (c, 3)]
runners = sorted(runners)

print('Times in ascending order:')
print(*[t for t, r in runners])

winner_time, winner = runners[0]
print(f'Runner {winner} won with {winner_time}')