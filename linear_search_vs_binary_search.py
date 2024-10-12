# Romain Tranchant
# CIS 103: Lab 5
# Instructor:MD Ali
# Lab: Exploring Searching, Sorting, and Algorithm Efficiency
# Due on Oct 12, 2024, 11:59 PM

# Activity:
# Write a Python function for linear search and binary search. Test both algorithms on the same
# sorted dataset (length = 1000)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            return -1


arr = list(range(1000))
target = 999

linear_result = linear_search(arr, target)
print(f"Linear search result is {linear_result}")

binary_result = binary_search(arr, target)
print(f"Binary search result is {binary_result}")

