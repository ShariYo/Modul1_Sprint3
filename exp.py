given = [7, 1, 3, 4, 1, 7]


def func(inp):
    results = []
    for first in range(len(inp)):
        for second in range(first + 1, len(inp)):
            if inp[first] == inp[second]:
                res = abs(first - second)
                results.append(res)
            else:
                pass

    return "-1" if not results else min(results)


print(func(given))
