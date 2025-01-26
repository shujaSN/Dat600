def InsertionSort(Input):
    CountSteps = 0  # count the number of steps
    for i in range(1, len(Input)):  # start from index 1, second element until length of input
        StartingElement = Input[i]  # store the element at index i
        j = i - 1  # store the element before the starting element

        # Move elements of input[0..i-1], that are greater than StartingElement, to one position ahead of their current position
        while j >= 0 and StartingElement < Input[j]:
            Input[j + 1] = Input[j]  # move the element to the right
            j -= 1  # decrement j
            CountSteps += 1

        Input[j + 1] = StartingElement
        CountSteps += 1
    return Input, CountSteps


def MergeSort(Input):
    CountSteps = 0  # count the number of steps
    if len(Input) <= 1:
        return Input, CountSteps

    # Divide the array into two halves
    middle = len(Input) // 2
    LeftSide = Input[:middle]
    RightSide = Input[middle:]

    LeftSide, LeftStep = MergeSort(LeftSide)
    RightSide, RightStep = MergeSort(RightSide)
    CountSteps += LeftStep + RightStep

    SortedElements = []
    i = j = 0

    # Comparing the elements from left and right side and adding them to the sorted elements array
    while i < len(LeftSide) and j < len(RightSide):
        CountSteps += 1
        if LeftSide[i] < RightSide[j]:
            SortedElements.append(LeftSide[i])
            i += 1
        else:
            SortedElements.append(RightSide[j])
            j += 1

    SortedElements += LeftSide[i:]
    SortedElements += RightSide[j:]
    CountSteps += len(SortedElements) - len(Input)  # count the number of steps

    return SortedElements, CountSteps


def HeapSortHeapify(Input, n, i, StepCount):
    LargestElement = i
    LeftChild = 2 * i + 1
    RightChild = 2 * i + 2

    # See if left child of root exists and is greater than root
    if LeftChild < n and Input[i] < Input[LeftChild]:
        LargestElement = LeftChild
        StepCount += 1

    # See if right child of root exists and is greater than root
    if RightChild < n and Input[LargestElement] < Input[RightChild]:
        LargestElement = RightChild
        StepCount += 1

    if LargestElement != i:  # if largest element is not root
        Input[i], Input[LargestElement] = Input[LargestElement], Input[i]
        StepCount += 3
        StepCount = HeapSortHeapify(Input, n, LargestElement, StepCount)
    return StepCount


def HeapSort(Input):
    n = len(Input)
    StepCount = 0
    # Building a maxheap
    i = n // 2 - 1
    while i >= 0:
        StepCount = HeapSortHeapify(Input, n, i, StepCount)
        i -= 1

    # Extract elements one by one from the heap and place it at the end of the array and heapify the remaining elements in the heap
    i = n - 1
    while i > 0:
        Input[i], Input[0] = Input[0], Input[i]
        StepCount += 3
        StepCount = HeapSortHeapify(Input, i, 0, StepCount)
        i -= 1

    return Input, StepCount


def QuickSort(Input):
    StepCount = 0
    if len(Input) <= 1:
        return Input, StepCount

    pivot = Input[-1]

    LeftSide = []
    RightSide = []

    # Loop through the input array and compare the elements with the pivot
    for i in Input[:-1]:  # exclude the pivot element
        if i < pivot:  # if element is less than pivot
            LeftSide.append(i)  # add it to the left side
        else:
            RightSide.append(i)  # add it to the right side

    LeftSorted, LeftSteps = QuickSort(LeftSide)
    RightSorted, RightSteps = QuickSort(RightSide)
    StepCount = LeftSteps + RightSteps + len(Input) - 1

    return LeftSorted + [pivot] + RightSorted, StepCount
