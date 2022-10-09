"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns, the robot can only
move in two directions, right and down, but certain cells are "off limits" such that robots can not step of them.
Design an algorithm to find a path for the robot from the top left to the bottom right. 
"""

def robot_in_grid(grid):
    if grid is None or len(grid) == 0:
        return None

    memo = {}
    path = []

    if get_path_in_grid(grid, len(grid) - 1, len(grid[0])-1, path, memo):
        return path
    return None

def get_path_in_grid(grid, row, col, path, memo):
    if row < 0 or col < 0:
        return False
    
    point = (row, col)
    
    if point in memo:
        return memo.get(point)
    
    if row == 0 and col == 0:
        path.append(point)
        memo[point] = True
        return True
    
    if get_path_in_grid(grid, row-1, col, path, memo) or \
            get_path_in_grid(grid, row, col-1, path, memo):
        path.append(point)
        memo[point] = True
        return True
    
    memo[point] = False
    return False