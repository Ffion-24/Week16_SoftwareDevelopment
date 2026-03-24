data = [2, 5, 7, 9, 12, 15, 18, 21]

data = [2, 5, 7, 9, 12, 15, 18, 21]

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def binary_search_with_counts(arr, target):
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        comparisons += 1
        if target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1, comparisons

print(binary_search(data, 9)) 
print(binary_search_with_counts(data, 9))