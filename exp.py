given = ["-3", "-2", "-1", "0", "1", "2"]
print(given)
fixed = list(map(int, given))
print(fixed)
intime = len([num for num in fixed if num <= 0])
print(intime)
