def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


# Example usage:
array = [9, 5, 1, 8, 3, 7, 4, 2, 6]
sorted_array = shell_sort(array)
print(sorted_array)
