# The purpose of this script is to take in three values
# to be converted to Hex
import math
def rgb(r, g, b):
    retVal = ""
    for x in [r,g,b]:
        if x<0: x=0
        elif x >255: x=255
        #left
        retVal += str(hex(math.floor((x)/16)))[2:].capitalize() 
        #right
        retVal += str(hex(x-(math.floor((x)/16)*16)))[2:].capitalize()
    return retVal

print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(255,255,255))
print(rgb(254,253,252))
print(rgb(-20,275,125))