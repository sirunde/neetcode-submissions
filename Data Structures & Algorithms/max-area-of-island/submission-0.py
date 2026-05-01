class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        n = len(grid)
        m = len(grid[0])
        queue = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    temp = 0

                    while(queue):
                        y,x = queue.pop()
                        if grid[y][x] == 1:
                            grid[y][x] = 0
                            temp += 1
                            if x<m-1 and grid[y][x+1] == 1:
                                queue.append((y,x+1))
                            if y<n-1 and grid[y+1][x] == 1:
                                queue.append((y+1,x))
                            if y>0 and grid[y-1][x] == 1:
                                queue.append((y-1,x))
                            if x>0 and grid[y][x-1] == 1:
                                queue.append((y,x-1))
                    maxi = max(maxi,temp)

        return maxi
