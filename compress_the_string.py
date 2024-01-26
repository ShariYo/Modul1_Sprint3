from itertools import groupby

count = []
for k, g in groupby(input()):
    key_and_group = (len(list(g)), int(k))
    count.append(key_and_group)

print(" ".join(map(str, count)))
