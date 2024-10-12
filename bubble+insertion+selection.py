# Romain Tranchant
# CIS 103: Lab 5
# Instructor:MD Ali
# Lab: Exploring Searching, Sorting, and Algorithm Efficiency
# Due on Oct 12, 2024, 11:59 PM


# Activity:
# Implement Bubble Sort, Insertion Sort, and Selection Sort in Python. Test them on the same
# dataset (length = 1000) and compare their run times.


import time

arr = list(range(1000)[::-1])

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]


start_bubble = time.time()
result_bubble = bubble_sort(arr)
end_bubble = time.time()
elapsed_bubble = end_bubble - start_bubble
print(f"Bubble sort in {elapsed_bubble:.9f} seconds")

start_insertion = time.time()
result_insertion = insertion_sort(arr)
end_insertion = time.time()
elapsed_insertion = end_insertion - start_insertion
print(f"Insertion sort in {elapsed_insertion:.9f} seconds")

start_selection = time.time()
result_selection = selection_sort(arr)
end_selection = time.time()
elapsed_selection = end_selection - start_selection
print(f"Selection sort in {elapsed_selection:.9f} seconds")