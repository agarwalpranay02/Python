"""
Binary Search (iterative)
Return index of target in sorted list, or -1 if not found.
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    data = [2, 4, 6, 8, 10, 12, 14]
    t = 10
    idx = binary_search(data, t)
    if idx != -1:
        print(f"Element found at index: {idx}")
    else:
        print("Element not found")
