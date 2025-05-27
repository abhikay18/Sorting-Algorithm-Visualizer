def bubble_sort(arr):
    """Generator function for bubble sort with step-by-step visualization"""
    n = len(arr)
    array = arr.copy()

    for i in range(n - 1):
        for j in range(n - i - 1):
            # Yield current state with comparing indices
            yield array.copy(), [j, j + 1], []

            if array[j] > array[j + 1]:
                # Swap elements
                array[j], array[j + 1] = array[j + 1], array[j]
                # Yield state after swap
                yield array.copy(), [], [j, j + 1]


def insertion_sort(arr):
    """Generator function for insertion sort with step-by-step visualization"""
    array = arr.copy()

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Yield current state
        yield array.copy(), [i], []

        while j >= 0 and array[j] > key:
            # Yield comparing state
            yield array.copy(), [j, j + 1], []

            array[j + 1] = array[j]
            # Yield after moving element
            yield array.copy(), [], [j, j + 1]
            j -= 1

        array[j + 1] = key


def selection_sort(arr):
    """Generator function for selection sort with step-by-step visualization"""
    array = arr.copy()
    n = len(array)

    for i in range(n - 1):
        min_idx = i

        # Yield current state
        yield array.copy(), [i], []

        for j in range(i + 1, n):
            # Yield comparing state
            yield array.copy(), [j, min_idx], []

            if array[j] < array[min_idx]:
                min_idx = j

        if min_idx != i:
            # Swap elements
            array[i], array[min_idx] = array[min_idx], array[i]
            # Yield after swap
            yield array.copy(), [], [i, min_idx]


def merge_sort(arr):
    """Generator function for merge sort with step-by-step visualization"""
    array = arr.copy()
    steps = []

    def merge_sort_helper(arr, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        merge_sort_helper(arr, start, mid)
        merge_sort_helper(arr, mid + 1, end)
        merge(arr, start, mid, end)

    def merge(arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            steps.append((arr.copy(), [k], []))

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

            steps.append((arr.copy(), [], [k - 1]))

        while i < len(left):
            arr[k] = left[i]
            steps.append((arr.copy(), [], [k]))
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            steps.append((arr.copy(), [], [k]))
            j += 1
            k += 1

    merge_sort_helper(array, 0, len(array) - 1)

    for step in steps:
        yield step


def quick_sort(arr):
    """Generator function for quick sort with step-by-step visualization"""
    array = arr.copy()
    steps = []

    def quick_sort_helper(arr, start, end):
        if start >= end:
            return

        pivot_index = partition(arr, start, end)
        quick_sort_helper(arr, start, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, end)

    def partition(arr, start, end):
        pivot_value = arr[end]
        pivot_index = start

        # Highlight pivot
        steps.append((arr.copy(), [end], []))

        for i in range(start, end):
            steps.append((arr.copy(), [i], []))

            if arr[i] < pivot_value:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                steps.append((arr.copy(), [], [i, pivot_index]))
                pivot_index += 1

        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        steps.append((arr.copy(), [], [pivot_index, end]))

        return pivot_index

    quick_sort_helper(array, 0, len(array) - 1)

    for step in steps:
        yield step
