from typing import List
def matrixReshape( mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        result = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                new_row = index // c
                new_col = index % c

                result[new_row][new_col] = mat[i][j]

        return result