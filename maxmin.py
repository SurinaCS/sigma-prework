def maxmin(numbers):
    """
    Function to return max and min of an array without using
    predefined max() and min()
    ARGS: 
    numbers (array) - numbers to find max and min 
    RETURNS:
    maxmin (array) - the maximum and minimum as [min, max]
    """
    arr_sorted = sorted(numbers)
    max = arr_sorted[-1]
    min = arr_sorted[0]
    return print([min, max])


arr = [1, 34, 6, 67, -100, 0]

maxmin(arr)
