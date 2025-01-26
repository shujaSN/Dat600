import random
import matplotlib.pyplot as plt
import time
import os
from sorting_algorithms import InsertionSort, MergeSort, HeapSort, QuickSort

# Create a directory to store plots if it doesn't exist
outputDir = "plots"
os.makedirs(outputDir, exist_ok=True)

inputSize = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,10000]  # Input sizes from 100 to 1000, step by 100

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
 
    start_time = time.time()
    _, steps = InsertionSort(input_array.copy())
    insertionSortTime.append(time.time() - start_time)
    insertionSortSteps.append(steps)

    # Merge Sort
    start_time = time.time()
    _, steps = MergeSort(input_array.copy())
    mergeSortTimes.append(time.time() - start_time)
    mergeSortSteps.append(steps)

    # Heap Sort
    start_time = time.time()
    _, steps = HeapSort(input_array.copy())
    heapSortTimes.append(time.time() - start_time)
    heapSortSteps.append(steps)

    # Quick Sort
    start_time = time.time()
    _, steps = QuickSort(input_array.copy())
    quickSortTimes.append(time.time() - start_time)
    quickSortSteps.append(steps)

# Plot Insertion Sort steps and time
plt.figure(figsize=(10, 6))
plt.plot(inputSize, insertionSortSteps, label="Insertion Sort - Steps", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Insertion Sort: Steps vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/insertion_steps_plot.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(inputSize, insertionSortTime, label="Insertion Sort - Time", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (seconds)")
plt.title("Insertion Sort: Time vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/insertionSortTime_plot.png")
plt.close()

# Plot Merge Sort steps and time
plt.figure(figsize=(10, 6))
plt.plot(inputSize, mergeSortSteps, label="Merge Sort - Steps", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Merge Sort: Steps vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/mergeSortSteps_plot.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(inputSize, mergeSortTimes, label="Merge Sort - Time", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (seconds)")
plt.title("Merge Sort: Time vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/mergeSortTimes_plot.png")
plt.close()

# Plot Heap Sort steps and time
plt.figure(figsize=(10, 6))
plt.plot(inputSize, heapSortSteps, label="Heap Sort - Steps", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Heap Sort: Steps vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/heapSortSteps_plot.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(inputSize, heapSortTimes, label="Heap Sort - Time", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (seconds)")
plt.title("Heap Sort: Time vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/heapSortTimes_plot.png")
plt.close()

# Plot Quick Sort steps and time
plt.figure(figsize=(10, 6))
plt.plot(inputSize, quickSortSteps, label="Quick Sort - Steps", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Quick Sort: Steps vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/quickSortSteps_plot.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(inputSize, quickSortTimes, label="Quick Sort - Time", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (seconds)")
plt.title("Quick Sort: Time vs Input Size")
plt.legend()
plt.grid(True)
plt.savefig(f"{outputDir}/quickSortTimes_plot.png")
plt.close()
