def linear_search(arr, target):
    for n in range(0, len(arr)):
      if arr[n] == target:
        return n


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
      mid = l + ( r - 1 ) // 2
      if arr[mid] == target:
        return mid
      elif arr[mid] < target:
        l = mid + 1
      else:
        r = mid - 1
    


    return -1  # not found
