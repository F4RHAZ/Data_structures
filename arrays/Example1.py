

def sum_pairs(A, target, k) -> list:
    if k > len(A):
        return -1

    current_sum = 0
    for i in range(0, len(A)):
        current_sum += A[i]
        if i >= k - 1:
            if current_sum == target:
                return [i, i - k + 1]
            else:
                current_sum -= A[i - (k - 1)]
    return sum_pairs(A, target, k + 1)


num = [2, 7, 11, 15]
target = 9
win_size = 2

print(sum_pairs(num, target, win_size))
