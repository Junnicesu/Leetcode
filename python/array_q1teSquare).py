class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        newList = []
        lenRow = len(matrix)
        lenColumn = len(matrix[0])
        for j in range(lenColumn):
            newList.append([matrix[i][j] for i in range(-1, -1-lenRow, -1)])

        for i in range(lenRow):
            for j in range(lenColumn):
                matrix[i][j] = newList[i][j]