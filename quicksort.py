# Author: Collin Smith
# Description: This program creates lists of integers to test sorting algorithms with.
import random
import time
import sys

sys.setrecursionlimit(10**6)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Generate randomg arrays.  Length of 1,000, 10,000, and 100,000.
# Max int of each array/list is 10,000.
array1k = [random.randint(0,10000) for i in range (1000)]
array10k = [random.randint(0,10000) for i in range (10000)]
array100k = [random.randint(0,10000) for i in range (100000)]

# Time insertion sort on random arrays.
start = time.time()
quickSort(array1k, 0, 999)
end = time.time()
print('Time elapsed for quickSort sort with 1,000 random ints: ', end - start)

start = time.time()
quickSort(array10k, 0, 9999)
end = time.time()
print('Time elapsed for quickSort sort with 10,000 random ints: ', end - start)

start = time.time()
quickSort(array100k, 0, 99999)
end = time.time()
print('Time elapsed for quickSort sort with 100,000 random ints: ', end - start)

# Sort arrays
array1k.sort()
array10k.sort()
array100k.sort()

# Time sorted arrays.
start = time.time()
quickSort(array1k, 0, 999)
end = time.time()
print('Time elapsed for quickSort sort with 1,000 sorted ints: ', end - start)

start = time.time()
quickSort(array10k, 0, 9999)
end = time.time()
print('Time elapsed for quickSort sort with 10,000 sorted ints: ', end - start)

start = time.time()
quickSort(array100k, 0, 99999)
end = time.time()
print('Time elapsed for quickSort sort with 100,000 sorted ints: ', end - start)



# Randomize 10th element.
for j in range (1, len(array1k)):
    if j % 10 == 0:
        array1k[j] = random.randint(0,1000)

for j in range (1, len(array10k)):
    if j % 10 == 0:
        array10k[j] = random.randint(0,1000)

for j in range (1, len(array100k)):
    if j % 10 == 0:
        array100k[j] = random.randint(0,1000)

# Time mostly sorted list.
start = time.time()
quickSort(array1k, 0, 999)
end = time.time()
print('Time elapsed for quickSort sort with 1,000 mostly sorted ints: ', end - start)

start = time.time()
quickSort(array10k, 0, 9999)
end = time.time()
print('Time elapsed for quickSort sort with 10,000 mostly sorted ints: ', end - start)

start = time.time()
quickSort(array100k, 0, 99999)
end = time.time()
print('Time elapsed for quickSort sort with 100,000 mostly sorted ints: ', end - start)
