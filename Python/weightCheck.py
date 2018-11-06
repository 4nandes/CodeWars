def getWeight(x):
    return sum(int(n) for n in str(x))
print(getWeight(23))
print(getWeight(444))
print(getWeight(12356))
