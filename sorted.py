def sorted(arr):
    # This recursive function sorts an array of integers using the quicksort algorithm.

    if len(arr) <= 1:
        # If there is only one element in the array or the array is empty, return it.
        return arr
    else:
        # Otherwise, choose the first element of the array as the pivot.
        pivot = arr[0]
        # Use a list comprehension to create two sub-arrays from the remaining elements.
        less_than_pivot = [i for i in arr[1:] if i <= pivot]
        more_than_pivot = [i for i in arr[1:] if i > pivot]
        # Recursively sort the sub-arrays and concatenate them with the pivot in the middle.
        return sorted(less_than_pivot) + [pivot] + sorted(more_than_pivot)