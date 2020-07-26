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

def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# 3 Sum total

def sum_total(lst):
    total = 0
    for val in lst:
        total += val
    return total

print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))


# 4 Average

def average(lst):
    total = 0
    for val in lst:
        total += val
    return float(total) / float(len(lst))

print(average([1 ,2 ,3 , 4]))

# 5 Length

def length(lst):
    # it is kind of cheating if we just return len(lst)
    # but this exercise is kind of silly
    count = 0
    for val in lst:
        count += 1
    return count

print(length([37, 2, 1, -9]))
print(length([]))


#6 Min
def minimum(lst):
    if len(lst) == 0:
        return False
    # we cannot use 0 in case all values are positive
    # if lst is empty, accessing lst[0] will throw an error
    # the conditional check and return statement above are crucial
    result = lst[0]
    for val in lst:
        if val < result:
            result = val
    return result

print(minimum([37, 2, 1, -9]))
print(minimum([]))

# 7 Max

def maximum(lst):
    if len(lst) == 0:
        return False

    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result

print(maximum([37, 2, 1, -9]))
print(maximum([]))

# 8 Ultimate Analysis

def ultimate_analysis(lst):
    # handle
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))

# 9 Reverse List

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        # this is a neat way to do a python swap, a temp is equally valid
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst


print(reverse_list([37, 2, 1, -9]))

