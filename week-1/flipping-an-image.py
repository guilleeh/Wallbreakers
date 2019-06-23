class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(A)):
            A[i].reverse()
            flipped_row = A[i]
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    flipped_row[j] = 1
                else:
                    flipped_row[j] = 0
            answer.append(flipped_row)
        return answer
