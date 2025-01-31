import random
import matplotlib.pyplot as plt
import time
import os
from sorting_algorithms import InsertionSort, MergeSort, HeapSort, QuickSort

# Create a directory to store plots if it doesn't exist
outputDir = "plots"
os.makedirs(outputDir, exist_ok=True)

inputSize = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000] 

insertionSortSteps = []
mergeSortSteps = []
heapSortSteps = []
quickSortSteps = []
insertionSortTime = []
mergeSortTimes = []
heapSortTimes = []
quickSortTimes = []

# Run tests for each input size
for size in inputSize:
    input_array = random.sample(range(1, size + 1), size)
    
    print(f"\nSorting array of size {size}:")

    # Insertion Sort
    start_time = time.time()
    _, steps = InsertionSort(input_array.copy())
    elapsed_time = time.time() - start_time
    insertionSortTime.append(elapsed_time)
    insertionSortSteps.append(steps)
    print(f"Insertion Sort Time: {elapsed_time:.6f} seconds")

    # Merge Sort
    start_time = time.time()
    _, steps = MergeSort(input_array.copy())
    elapsed_time = time.time() - start_time
    mergeSortTimes.append(elapsed_time)
    mergeSortSteps.append(steps)
    print(f"Merge Sort Time: {elapsed_time:.6f} seconds")

    # Heap Sort
    start_time = time.time()
    _, steps = HeapSort(input_array.copy())
    elapsed_time = time.time() - start_time
    heapSortTimes.append(elapsed_time)
    heapSortSteps.append(steps)
    print(f"Heap Sort Time: {elapsed_time:.6f} seconds")

    # Quick Sort
    start_time = time.time()
    _, steps = QuickSort(input_array.copy())
    elapsed_time = time.time() - start_time
    quickSortTimes.append(elapsed_time)
    quickSortSteps.append(steps)
    print(f"Quick Sort Time: {elapsed_time:.6f} seconds")

# Save execution time results to a text file
with open(f"{outputDir}/execution_times.txt", "w") as f:
    f.write("Input Size, Insertion Sort, Merge Sort, Heap Sort, Quick Sort\n")
    for i in range(len(inputSize)):
        f.write(f"{inputSize[i]}, {insertionSortTime[i]:.6f}, {mergeSortTimes[i]:.6f}, {heapSortTimes[i]:.6f}, {quickSortTimes[i]:.6f}\n")

print("\nExecution times saved to execution_times.txt")
