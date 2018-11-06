def getWeight(x,y):
    if (sum(int(n) for n in str(y)) - sum(int(n) for n in str(x))) == 0:
        return min(x,y)
    else:
        return sum(int(n) for n in str(y)) - sum(int(n) for n in str(x)) 

def order_weight(string):
    test = [x for x in string.split(None)]
    print(" ".join(sorted(test, cmp=getWeight)))

order_weight("103 123 4444 99 2000")