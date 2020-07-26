# 1 Biggie Size 
def big(NumList):
    newList=[]
    for y in range(len(NumList)):
        if NumList[y] > 0:
            NumList[y] = "big"
            newList.append(NumList[y])
    return NumList

print(big([-1, 3, 5, -5]))

# 2 Count Positives

