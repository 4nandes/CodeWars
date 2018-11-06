def dashatize(num):

    retVal =""
    try:
        for x in str(num).replace("-",""):
            if (int(x)%2 ==0):
                retVal += x
            else:
                if retVal.endswith("-") or retVal == "":
                    retVal += "{}-".format(x)
                else:
                    retVal += "-{}-".format(x)
    except ValueError:
        return 
    if retVal.endswith("-"):
        return retVal[:-1]
    return(retVal)

print(dashatize(274))
print(dashatize(274))
print(dashatize(5311))
print(dashatize(86320))
print(dashatize(974302))
print(dashatize(None))