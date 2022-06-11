from util import time_func, randomGen

def swap(a,b, arr):
    if a!= b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(items, start, end):
    pivot_index = start
    pivot = items[pivot_index]

    while start < end:
        while start< len(items) and items[start] <= pivot:
            start += 1

        while items[end] > pivot:
            end -=1

        if start < end:
            swap(start , end, items)

    swap(pivot_index, end, items)

    return end

def quickSort(items, start, end):
    if start < end:
        p1 = partition(items, start, end)
        quickSort(items, start, p1 -1) #left partition
        quickSort(items, p1+1, end) #right partition





x = [52, 78, 98, 11, 63, 89, 5, 2]

test = [
    [11,9,29,7,2,15,28],
    [3,7,9,11],
    [25,22,21,10],
    [],
    [6]
]


quickSort(x , 0 , len(x)-1 )
print(x)

for each in test:
    quickSort(each, 0, len(each)-1)
    print(f'Sorted Array: {each}')