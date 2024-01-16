def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            # Element found
            return iterations, arr[mid]

    # If the target is not in the array, return the upper bound
    upper_bound = arr[left] if left < len(arr) else None
    return iterations, upper_bound


# Example usage:
sorted_array = [0.1, 0.3, 0.5, 1.2, 1.5, 1.7, 2.0, 2.5, 3.1, 4.0, 4.5, 5.2, 7]
target_value = 2.0

iterations, upper_bound = binary_search(sorted_array, target_value)

if upper_bound is not None:
    print(f"Number of iterations: {iterations}, Upper bound: {upper_bound}")
else:
    print(f"Number of iterations: {iterations}, Target value not found")
