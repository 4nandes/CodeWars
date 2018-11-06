def stringSplitter(content):
    lump = ""
    lumpList = []
    for e in content:
        if len(lump) == 1:
            lump = lump + e
            lumpList.append(lump)
            lump = ""
        else:
            lump = e
    
    if len(lump) == 1:
            lump = lump + '_'
            lumpList.append(lump)
            lump = ""
    return lumpList
    

print(stringSplitter("asdfasdf"))

print(stringSplitter("asdfads"))

print(stringSplitter(""))