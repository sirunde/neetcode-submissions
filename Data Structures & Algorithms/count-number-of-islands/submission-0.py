from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        n = len(grid)
        m = len(grid[0])

        been = [[False]*m for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not been[i][j]:
                    queue.append((i,j))
                    islands += 1

                    while(queue):
                        y,x = queue.popleft()

                        been[y][x] = True
                        if x<m-1 and grid[y][x+1] == "1" and not been[y][x+1]:
                            queue.append((y,x+1))
                        if y<n-1 and grid[y+1][x] == "1" and not been[y+1][x]:
                            queue.append((y+1,x))
                        if y>0 and grid[y-1][x] == "1" and not been[y-1][x]:
                            queue.append((y-1,x))
                        if x>0 and grid[y][x-1] == "1" and not been[y][x-1]:
                            queue.append((y,x-1))

        return islands
                    

