def find_outlier(integers):
    odds = []
    evens = []
    for x in integers:
        if (x%2 == 0):
            evens.append(x)
        else:
            odds.append(x)
    if len(evens) == 1:
        return evens[0]
    else:
        return odds[0]

print(find_outlier([1, 2, 2]))
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))