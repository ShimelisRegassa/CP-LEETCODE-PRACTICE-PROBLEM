# Merge Sorted Array (LeetCode)

* **Difficulty:** Easy
* **Platform:** LeetCode [Problem Link](https://leetcode.com/problems/merge-sorted-array/)
* **Language:** Python 3

## Problem Description
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored *inside* the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored.

## Approach
1. **Two-Pointer Technique:** Maintain two pointers (`left1` and `left2`) to iterate through the valid elements of `nums1` and `nums2` simultaneously.
2. **Comparison & Merging:** Compare the elements at both pointers. Append the smaller element to a temporary `result` list and increment the corresponding pointer.
3. **Handling Remaining Elements:** Once one of the arrays is fully traversed, append any remaining elements from the other array to the `result` list.
4. **In-Place Modification:** Copy the contents of the `result` list back into `nums1` using slice assignment (`nums1[:] = result`) to satisfy the in-place modification requirement.

## Complexity Analysis
* **Time Complexity:** $O(m + n)$ — We iterate through both arrays once to merge them.
* **Space Complexity:** $O(m + n)$ — A temporary `result` list is used to store the merged elements before updating `nums1` in place.

## Python Implementation
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1 = 0
        left2 = 0
        result = []

        while left1 <= m - 1 and left2 <= n - 1:
            if nums1[left1] <= nums2[left2]:
                result.append(nums1[left1])
                left1 += 1
            else:
                result.append(nums2[left2])
                left2 += 1
                
        while left1 < m:
            result.append(nums1[left1])
            left1 += 1
            
        while left2 < n:
            result.append(nums2[left2])
            left2 += 1
            
        nums1[:] = result