'''
# QUESTION:

Given an array of integers nums and an integer target, return the
indices of two numbers such that they add up to target

You may assume that each input would have exaclty one solution
And you may not use not use same element twice

You can return the answer in any order


Example 1
input: nums = [2,7,11,15], target = 9
output: [0,1]

Example 2
inputs: nums = [3,2,4], target = 6
Output: [1,2]

Example 3
Input: nums = [3,3], target = 6
Output: [0,1]

'''


################################################
#
#    BRUTE FORCE APPROACH
#
################################################\


def sumPairs(arr, target):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
                break

arr =  [3,2,4]
target = 6

print(sumPairs(arr, target))

################################################
#
#    ABOVE SOLUTION HAS O(n^2) time complexity
#      needs to be optimized
#
################################################
