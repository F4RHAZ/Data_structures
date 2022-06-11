from util import time_func, randomGen

'''
def mergeSortedArray(a,b):
    sortedList = []
    len_a = len(a)
    len_b = len(b)
    i=j=0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sortedList.append(a[i])
            i += 1
        else:
            sortedList.append(b[j])
            j+= 1

    while i < len_a:
        sortedList.append(a[i])
        i += 1
    while j < len_b:
        sortedList.append(b[j])
        j += 1

    return sortedList


def mergerSort(items):
    if len(items) <= 1:
        return items

    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]

    left = mergerSort(left)
    right = mergerSort(right)

    return mergeSortedArray(left, right)


x = randomGen(100)
a = [5,8,12,56]
b = [7,9,45,51]

print(mergeSortedArray(a,b))

print(mergerSort(x))
'''

'''
ISSUES WITH ABOVE CODE IS SPACE
'''


def mergeSortedArray(a,b, items):

    len_a = len(a)
    len_b = len(b)
    i=j=k=0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            items[k] = a[i]
            i += 1
        else:
            items[k] = b[j]
            j+= 1
        k += 1

    while i < len_a:
        items[k] = a[i]
        i += 1
        k+=1
    while j < len_b:
        items[k] = b[j]
        j += 1
        k+1



def mergeSort(items):
    if len(items) <= 1:
        return
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    mergeSort(left)
    mergeSort(right)

    mergeSortedArray(left, right, items)



x = randomGen(100)
print(x)
mergeSort(x)
print(x)

