# 1 Countdown

a = input('input your number here: ')


def countDown(a):
    numList = []
    for val in range(int(a), -1, -1):
        numList.append(val)
    return numList


print(countDown(a))

# 2 Print and Return

def printReturn(NList):

    print(NList[0])
    return (NList[1])

print(printReturn([1, 2]))

# 3 First Plus Length

def length(nums_list):
    x = (nums_list[0])
    y = len(nums_list)
    z = x + y
    return z

print(length([1,2,3,4,5]))
