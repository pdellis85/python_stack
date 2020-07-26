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


# 4 Values Greater than Second

def val_sec(numList):
  newList=[]
  x = (numList[1])
  for y in range(len(numList)):
    if numList[y] > x:
      newList.append(numList[y])
  print(len(newList))
  return newList
print(val_sec([5,2,3,2,1,4]))

# 5 This Length, That Value

def length_and_value(size, value):
    new_list = []
    for y in range(size):
        new_list.append(value)
    return new_list

print(length_and_value(4,7))