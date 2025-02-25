"""
Main interface for the flood fill algorithm demonstration.
This file provides an interactive command-line interface for running
the flood fill algorithm on various example grids or custom grids.
"""

import time
from collections import deque
import floodfill
import visualizer
import examples

def run_interactive_demo():
    """
    Run an interactive demonstration of the flood fill algorithm.
    
    This function guides the user through selecting an example grid or
    creating their own, choosing fill parameters, and visualizing the results.
    """
    # Initialize the visualizer
    vis = visualizer.FloodFillVisualizer(use_blocks=True)
    
    print("=" * 60)
    print("Flood Fill Algorithm Demonstration")
    print("=" * 60)
    print("\nThis program demonstrates the flood fill algorithm using BFS.")
    print("It's similar to the 'paint bucket' tool in graphic editors.\n")
    
    # Present example options
    print("Choose an example grid or create your own:")
    print("1. Use an example grid")
    print("2. Create a custom grid")
    
    choice = input("\nEnter your choice (1/2): ").strip()
    
    # Handle grid selection
    if choice == "1":
        examples.print_available_examples()
        example_choice = input("\nSelect an example number: ").strip()
        
        try:
            example_index = int(example_choice) - 1
            example_names = list(examples.get_all_examples().keys())
            selected_example = example_names[example_index]
            grid = examples.get_all_examples()[selected_example]
            print(f"\nSelected example: {selected_example}")
        except (ValueError, IndexError):
            print("\nInvalid selection. Using landscape example.")
            grid = examples.LANDSCAPE
    else:
        print("\nCreating a custom grid. Enter each row as a string of characters.")
        print("Use hyphen '-' for empty spaces and any other character for filled spaces.")
        print("Enter a blank line when finished.")
        
        custom_grid = []
        while True:
            row = input("Enter row (or blank to finish): ").strip()
            if not row:
                break
            custom_grid.append(list(row))
        
        if not custom_grid:
            print("\nNo grid provided. Using a simple square example.")
            grid = examples.SIMPLE_SQUARE
        else:
            grid = custom_grid
    
    # Show the selected grid
    print("\nInitial Grid:")
    vis.print_colored_grid(grid)
    
    # Get fill parameters
    try:
        start_row = int(input("\nStart point row number: "))
        start_col = int(input("Start point column number: "))
        
        # Validate coordinates
        if not (0 <= start_row < len(grid) and 0 <= start_col < len(grid[0])):
            raise IndexError("Coordinates out of bounds")
        
        new_shape = input("New filling shape X 🟥 ; O 🟩 ; - ⬜ ; # 🟨 ; @ 🟦 ; * 🟪 ; + 🟫  :  ")
        if len(new_shape) != 1:
            new_shape = 'O'  # Default if not a single character
            print("Using 'O' as the fill character.")
        
        animate = input("Animate the fill process? (y/n): ").lower() == 'y'
        
        # Get animation speed if animating
        delay = 0.05
        if animate:
            try:
                speed = input("Animation speed (1=slow, 5=fast): ").strip()
                if speed:
                    delay = 0.2 / int(speed)  # Convert speed to delay
            except ValueError:
                print("Using default animation speed.")
        
        # Execute the flood fill
        print("\nPerforming flood fill...\n")
        
        # Track performance statistics
        start_time = time.time()
        cells_filled = floodfill.perform_flood_fill(
            grid, 
            start_row, 
            start_col, 
            new_shape,
            animate=animate,
            visualizer=vis,
            delay=delay
        )
        end_time = time.time()
        
        # Print the final result if not animated
        if not animate:
            print("Final Result:")
            vis.print_colored_grid(grid)
        
        # Display statistics
        stats = {
            "cells_filled": cells_filled,
            "time_taken": end_time - start_time,
        }
        vis.display_stats(stats)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter valid numbers for row and column.")
    except IndexError as e:
        print(f"\nError: {e}")
        print("The coordinates you entered are outside the grid boundaries.")
    
    # Ask if user wants to try again
    again = input("\nWould you like to try another example? (y/n): ").lower() == 'y'
    if again:
        run_interactive_demo()
    else:
        print("\nThank you for trying the Flood Fill Algorithm Demonstration!")

if __name__ == "__main__":
    run_interactive_demo()