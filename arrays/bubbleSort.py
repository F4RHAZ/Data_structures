from util import time_func, randomGen

@time_func
def bubbleSort(elements):
    size = len(elements)
    for j in range(size-1):
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
    return elements

x = randomGen()
print(x)
sorted = bubbleSort(x)
print(sorted)
print("Trying to sort a sorted List ")
bubbleSort(sorted)

# As seen in the above code the sorted array is still sorted
# Implement a check to see if the list is sorted

@time_func
def bubble_Sort(items):
    size = len(items)
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                swapped = True
        if not swapped:
            break

print("\nKnowing that a list is sorted helps reduce taversal time ")
bubble_Sort(sorted)

'''
THE ABOVE CODE CAN STILL BE IMPROVED SINCE EVERY ITERATION THE LARGEST NUMBER REACHES THE RIGHT POSITION
HENCE WHENEVER WE ITERATE IN THE SECOND LOOP WE REDUCE THE SIZE OF THE LIST 
IMPLEMENTED IN THE CODE BELOW

'''
@time_func
def bubbleSortImproved(elements):
    size = len(elements)
    for j in range(size-1):
        for i in range(size-1-j):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
    return elements

z = randomGen()

bubbleSortImproved(z)