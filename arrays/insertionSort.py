from util import time_func, randomGen

@time_func
def insertionSort(items):
    for i in range(1, len(items)):
        anchor = items[i]
        j = i -1
        while j >= 0 and anchor < items[j]:
            items[j+1] = items[j]
            j = j -1
        items[j+1] = anchor

x = randomGen(10000)

insertionSort(x)
print(x)