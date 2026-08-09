# Last updated: 10/08/2026, 02:35:45
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0]) 
        # this is how we get the value of a column in a grid.
        islandCount = 0
        visited = set()
        # Direction vectors
        dirs = [(-1,0),(1,0),(0,-1),(0,1)] 
        # These co-ordinates are according to rows and colums not according to (x,y) co-ordinates in maths.
        def BFS(R,C):
            # Create a queue
            q = collections.deque()
            # Append the starting rows and columns to the queue
            q.append((R,C))
            # Add the rows and colums to the visited set
            visited.add((R,C))
            while q:
                R, C = q.popleft()
                # Explore all 4 neighbors
                for directionRows, directionColumns in dirs:
                    newRow, newColumn = R + directionRows, C + directionColumns
                    # Check in-bounds, is land, and unvisited
                    if(0 <= newRow < rows and 0 <= newColumn < cols 
                    and grid[newRow][newColumn] == "1"
                    and (newRow,newColumn) not in visited):
                        visited.add((newRow,newColumn))
                        q.append((newRow,newColumn))

        # Main loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islandCount += 1
                    BFS(r,c)
        
        return islandCount


        