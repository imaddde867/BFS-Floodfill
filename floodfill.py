"""
Core implementation of the flood fill algorithm using Breadth-First Search (BFS).
"""

from collections import deque

def perform_flood_fill(grid, start_row, start_col, new_shape, animate=False, visualizer=None, delay=0.05):
    """
    Perform flood fill algorithm starting from a specific point.
    
    This implementation uses Breadth-First Search (BFS) to efficiently
    replace all connected cells matching the original value with a new value.
    
    Args:
        grid (List[List[str]]): The 2D grid to perform flood fill on
        start_row (int): Starting row index
        start_col (int): Starting column index
        new_shape (str): The new value to fill with
        animate (bool): Whether to animate the fill process
        visualizer: Visualizer object for displaying the process
        delay (float): Delay between animation frames in seconds
        
    Returns:
        int: Number of cells that were filled
    """
    # Get dimensions
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    # Validate input coordinates
    if not (0 <= start_row < height and 0 <= start_col < width):
        raise IndexError("Starting coordinates are outside the grid")
    
    # Get the original shape at the starting point
    original_shape = grid[start_row][start_col]
    
    # Early return if starting cell is already the new shape
    if original_shape == new_shape:
        return 0
    
    # Initialize queue for BFS
    queue = deque([(start_row, start_col)])
    
    # Define possible movement directions (up, down, right, left)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # Keep track of visited cells to avoid revisiting
    visited = set([(start_row, start_col)])
    
    # Counter for number of cells filled
    cells_filled = 0
    
    # Process cells until queue is empty
    while queue:
        # Get the next cell
        row, col = queue.popleft()
        
        # Check if the cell should be filled
        if grid[row][col] == original_shape:
            # Fill the cell
            grid[row][col] = new_shape
            cells_filled += 1
            
            # If animation is enabled, show the current state
            if animate and visualizer:
                visualizer.animate_fill(grid, delay)
            
            # Add all valid neighboring cells to the queue
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the neighbor is within bounds and not visited
                if (0 <= new_row < height and 
                    0 <= new_col < width and 
                    (new_row, new_col) not in visited and
                    grid[new_row][new_col] == original_shape):
                    
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
    
    return cells_filled

def flood_fill_diagonal(grid, start_row, start_col, new_shape, animate=False, visualizer=None, delay=0.05):
    """
    Perform flood fill algorithm including diagonal neighbors.
    
    This is an extension of the standard flood fill that also considers
    diagonal neighboring cells (8 directions total).
    
    Args:
        grid (List[List[str]]): The 2D grid to perform flood fill on
        start_row (int): Starting row index
        start_col (int): Starting column index
        new_shape (str): The new value to fill with
        animate (bool): Whether to animate the fill process
        visualizer: Visualizer object for displaying the process
        delay (float): Delay between animation frames in seconds
        
    Returns:
        int: Number of cells that were filled
    """
    # Get dimensions
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    # Validate input coordinates
    if not (0 <= start_row < height and 0 <= start_col < width):
        raise IndexError("Starting coordinates are outside the grid")
    
    # Get the original shape at the starting point
    original_shape = grid[start_row][start_col]
    
    # Early return if starting cell is already the new shape
    if original_shape == new_shape:
        return 0
    
    # Initialize queue for BFS
    queue = deque([(start_row, start_col)])
    
    # Define possible movement directions (8 directions including diagonals)
    directions = [
        (-1, 0), (1, 0), (0, 1), (0, -1),    # Cardinal directions
        (-1, -1), (-1, 1), (1, -1), (1, 1)   # Diagonal directions
    ]
    
    # Keep track of visited cells to avoid revisiting
    visited = set([(start_row, start_col)])
    
    # Counter for number of cells filled
    cells_filled = 0
    
    # Process cells until queue is empty
    while queue:
        # Get the next cell
        row, col = queue.popleft()
        
        # Check if the cell should be filled
        if grid[row][col] == original_shape:
            # Fill the cell
            grid[row][col] = new_shape
            cells_filled += 1
            
            # If animation is enabled, show the current state
            if animate and visualizer:
                visualizer.animate_fill(grid, delay)
            
            # Add all valid neighboring cells to the queue
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the neighbor is within bounds and not visited
                if (0 <= new_row < height and 
                    0 <= new_col < width and 
                    (new_row, new_col) not in visited and
                    grid[new_row][new_col] == original_shape):
                    
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
    
    return cells_filled

def flood_fill_with_boundary(grid, start_row, start_col, new_shape, 
                            boundary_shape=None, animate=False, visualizer=None, delay=0.05):
    """
    Perform flood fill algorithm with boundary detection.
    
    This version can stop at a specified boundary shape, useful for
    filling within enclosed regions.
    
    Args:
        grid (List[List[str]]): The 2D grid to perform flood fill on
        start_row (int): Starting row index
        start_col (int): Starting column index
        new_shape (str): The new value to fill with
        boundary_shape (str): The boundary value to stop at (None to use any non-matching)
        animate (bool): Whether to animate the fill process
        visualizer: Visualizer object for displaying the process
        delay (float): Delay between animation frames in seconds
        
    Returns:
        int: Number of cells that were filled
    """
    # Get dimensions
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    # Validate input coordinates
    if not (0 <= start_row < height and 0 <= start_col < width):
        raise IndexError("Starting coordinates are outside the grid")
    
    # Get the original shape at the starting point
    original_shape = grid[start_row][start_col]
    
    # Early return if starting cell is already the new shape or is the boundary
    if original_shape == new_shape or (boundary_shape and original_shape == boundary_shape):
        return 0
    
    # Initialize queue for BFS
    queue = deque([(start_row, start_col)])
    
    # Define possible movement directions (up, down, right, left)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # Keep track of visited cells to avoid revisiting
    visited = set([(start_row, start_col)])
    
    # Counter for number of cells filled
    cells_filled = 0
    
    # Process cells until queue is empty
    while queue:
        # Get the next cell
        row, col = queue.popleft()
        
        # Check if the cell should be filled
        if grid[row][col] == original_shape:
            # Fill the cell
            grid[row][col] = new_shape
            cells_filled += 1
            
            # If animation is enabled, show the current state
            if animate and visualizer:
                visualizer.animate_fill(grid, delay)
            
            # Add all valid neighboring cells to the queue
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the neighbor is within bounds and not visited
                if (0 <= new_row < height and 
                    0 <= new_col < width and 
                    (new_row, new_col) not in visited):
                    
                    # If boundary shape is specified, skip cells with that value
                    if boundary_shape and grid[new_row][new_col] == boundary_shape:
                        continue
                    
                    # Add cell to queue if it has the original shape
                    if grid[new_row][new_col] == original_shape:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
    
    return cells_filled