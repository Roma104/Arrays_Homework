def second_largest(arr):
    """Return the second largest number in the list."""
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1]

def median(arr):
    """Return the median of the list."""
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]

def min_max(arr):
    """Return a tuple with the smallest and largest number in the list."""
    return min(arr), max(arr)

def numbers_as_string(arr):
    """Return the list of numbers as a single concatenated string."""
    return "".join(map(str, arr))
