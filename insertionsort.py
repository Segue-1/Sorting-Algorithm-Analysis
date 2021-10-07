# Author: Collin Smith
# Description: This program creates lists of integers to test sorting algorithms with.
import random
import time

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate randomg arrays.  Length of 1,000, 10,000, and 100,000.
# Max int of each array/list is 10,000.
array1k = [random.randint(0,10000) for i in range (1000)]
array10k = [random.randint(0,10000) for i in range (10000)]
array100k = [random.randint(0,10000) for i in range (100000)]

# Time insertion sort on random arrays.
start = time.time()
insertionSort(array1k)
end = time.time()
print('Time elapsed for insertion sort with 1,000 random ints: ', end - start)

start = time.time()
insertionSort(array10k)
end = time.time()
print('Time elapsed for insertion sort with 10,000 random ints: ', end - start)

start = time.time()
insertionSort(array100k)
end = time.time()
print('Time elapsed for insertion sort with 100,000 random ints: ', end - start)

# Sort arrays
array1k.sort()
array10k.sort()
array100k.sort()

# Time sorted arrays.
start = time.time()
insertionSort(array1k)
end = time.time()
print('Time elapsed for insertion sort with 1,000 sorted ints: ', end - start)

start = time.time()
insertionSort(array10k)
end = time.time()
print('Time elapsed for insertion sort with 10,000 sorted ints: ', end - start)

start = time.time()
insertionSort(array100k)
end = time.time()
print('Time elapsed for insertion sort with 100,000 sorted ints: ', end - start)



# Randomize 10th element.
for j in range (1, len(array1k)):
    if j % 10 == 0:
        array1k[j] = [random.randint(0,1000)]

for j in range (1, len(array10k)):
    if j % 10 == 0:
        array10k[j] = [random.randint(0,1000)]

for j in range (1, len(array100k)):
    if j % 10 == 0:
        array100k[j] = [random.randint(0,1000)]

# Time mostly sorted list.
start = time.time()
insertionSort(array1k)
end = time.time()
print('Time elapsed for insertion sort with 1,000 mostly sorted ints: ', end - start)

start = time.time()
insertionSort(array10k)
end = time.time()
print('Time elapsed for insertion sort with 10,000 mostly sorted ints: ', end - start)

start = time.time()
insertionSort(array100k)
end = time.time()
print('Time elapsed for insertion sort with 100,000 mostly sorted ints: ', end - start)


