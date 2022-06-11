import random
import time

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " Took " + str((end-start)*1000) + " Milliseconds ")
        return result
    return wrapper


def randomGen(length):
    randomList = []
    for i in range(0, length):
        n = random.randint(1 , 100001)
        randomList.append(n)
    return randomList