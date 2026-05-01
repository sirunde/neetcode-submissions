class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we need loop twice
        # first find the correct row
        # find the correct column
        n = len(matrix)
        m = len(matrix[0])-1

        i = 0 # i is the row 
        j = 0 # j is column

        midIdx = (i+n)//2
        midJdx = (j+m)//2
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False

        while(i+1<n):
            if matrix[midIdx][0] > target:
                n = midIdx

            elif matrix[midIdx][0] < target:
                i = midIdx
            else:
                return True
            midIdx = (i+n)//2

        while(j<=m):
            if matrix[midIdx][midJdx] > target:
                m = midJdx-1
            elif matrix[midIdx][midJdx] < target:
                j = midJdx+1
            else:
                return True
            midJdx = (j+m)//2

        return False
        

