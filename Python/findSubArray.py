# Find the largest subArray
# ________________
# Plan of attack:
# _______________
# -Use recursion
# -use the negative numbers as points of interest when determining the next subarray to compare
# -Recurse till the array is at its smallest and then return the value that we get
# -Maybe pass around the largest sum that we have found so far so that at the end we can return that value
# _________________
# INITIAL ATTEMPT BELOW
# Works great for the example, but the problem is much larger than the example
#_______________________________________________________________________________
# def maxSequence(arr,highscore=0):

#     if sum(arr) > highscore:
#         highscore = sum(arr)


#     leftIndex = 0
#     for x in arr:
#         if x < 0:           
#             break
#         leftIndex += 1
#     if sum(arr[:leftIndex+1]) < 0:
#         leftIndex += 1
#     else:
#         leftIndex = 0
    
#     rightIndex = len(arr) -1
#     for x in arr[::-1]:
#         if x < 0:
#             break
#         rightIndex -= 1
        
#     if sum(arr[:rightIndex-1:-1]) < 0:
#         rightIndex -= 1
#     else:
#         rightIndex = len(arr) 
    
#     if len(arr) == 0 or arr[leftIndex:rightIndex+1] == arr:
#         return highscore
#     else:
#         return maxSequence(arr[leftIndex:rightIndex+1],highscore)

def maxSequence(arr):
    stoppingIndex = 0
    for x in arr:
        print("Full Array: ",arr[0:stoppingIndex + 1], "\nX: ",x)
        if x >= 0:
            stoppingIndex += 1
        
        elif sum(arr[0:stoppingIndex + 1]) > 0:
            break
    # print(arr[stoppingIndex:])


maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])