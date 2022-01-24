def  countdown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countdown(5))


def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,2]))


def first_plus_length(list):
    return len(list) + list[0]
print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


def length_and_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))