def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(items, start, end):
    pivot_index = start
    pivot = items[pivot_index]

    while start < end:
        while items[start] <= pivot:
            start += 1

        while items[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, items)

    swap(pivot_index, end, items)
    return end


def quickSort(items, start, end):
    if start < end:
        p1 = partition(items, start, end)
        quickSort(items, start, p1 - 1)  # left partition
        quickSort(items, p1 + 1, end)  # right partition


x = [11, 23, 456, 1, 2, 4, 67, 9, 0]
print(x)
quickSort(x, 0, len(x) - 1)
print(x)