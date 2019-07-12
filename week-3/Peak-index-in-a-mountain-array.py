class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A) - 1
        while left < right:
            pivot = (left + right) // 2
            if A[pivot] < A[pivot + 1]:
                left = pivot + 1
            else:
                right = pivot
        return left
