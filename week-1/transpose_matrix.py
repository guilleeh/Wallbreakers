class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transpose = []
        for outer in range(len(A[0])):
            row = []
            for inner in range(len(A)):
                row.append(A[inner][outer])
            transpose.append(row)
        return transpose

