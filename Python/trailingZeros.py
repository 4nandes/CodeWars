import math

def zeros(n):
    if n == 0 : return 0
    retVal = 0
    x = 1
    while x <= math.floor(math.log(n,5)):
        print(5**x)
        print(math.floor(n/(5**x)))
        retVal += math.floor(n/(5**x))
        x += 1
    return retVal




print(zeros(777))