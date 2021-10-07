# Author: Collin Smith
# Description: This program creates lists of integers to test sorting algorithms with.
import random
import time

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Generate randomg arrays.  Length of 1,000, 10,000, and 100,000.
# Max int of each array/list is 10,000.
array1k = [random.randint(0,10000) for i in range (1000)]
array10k = [random.randint(0,10000) for i in range (10000)]
array100k = [random.randint(0,10000) for i in range (100000)]

# Time insertion sort on random arrays.
start = time.time()
mergeSort(array1k)
end = time.time()
print('Time elapsed for mergeSort sort with 1,000 random ints: ', end - start)

start = time.time()
mergeSort(array10k)
end = time.time()
print('Time elapsed for mergeSort sort with 10,000 random ints: ', end - start)

start = time.time()
mergeSort(array100k)
end = time.time()
print('Time elapsed for mergeSort sort with 100,000 random ints: ', end - start)

# Sort arrays
array1k.sort()
array10k.sort()
array100k.sort()

# Time sorted arrays.
start = time.time()
mergeSort(array1k)
end = time.time()
print('Time elapsed for mergeSort sort with 1,000 sorted ints: ', end - start)

start = time.time()
mergeSort(array10k)
end = time.time()
print('Time elapsed for mergeSort sort with 10,000 sorted ints: ', end - start)

start = time.time()
mergeSort(array100k)
end = time.time()
print('Time elapsed for mergeSort sort with 100,000 sorted ints: ', end - start)



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
mergeSort(array1k)
end = time.time()
print('Time elapsed for mergeSort sort with 1,000 mostly sorted ints: ', end - start)

start = time.time()
mergeSort(array10k)
end = time.time()
print('Time elapsed for mergeSort sort with 10,000 mostly sorted ints: ', end - start)

start = time.time()
mergeSort(array100k)
end = time.time()
print('Time elapsed for mergeSort sort with 100,000 mostly sorted ints: ', end - start)
