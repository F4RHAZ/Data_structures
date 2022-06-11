def shellSort(items):
    size = len(items)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = items[i]
            j = i
            while j >= gap and items[j - gap] > anchor:
                items[j] = items[j - gap]
                j -= gap
            items[j] = anchor
        gap = gap // 2


z = [11, 23, 456, 1, 2, 4, 67, 9, 0]

shellSort(z)

print(z)