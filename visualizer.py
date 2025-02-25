# visualizer.py

import os
import time
from colorama import init, Fore, Style, Back

# Initialize colorama for cross-platform colored terminal output
init()

class FloodFillVisualizer:
    """
    Provides visualization tools for the flood fill algorithm.
    
    This class handles different ways to display the grid, including:
    - Plain text visualization
    - Color-coded visualization
    - Animated visualization of the fill process
    """
    
    def __init__(self, use_emojis=False, use_blocks=True):
        """
        Initialize the visualizer with display preferences.
        
        Args:
            use_emojis (bool): Whether to use emoji characters for visualization
            use_blocks (bool): Whether to use block characters instead of original characters
        """
        self.use_emojis = use_emojis
        self.use_blocks = use_blocks
        
        # Define color mappings for different cell values
        self.colors = {
            'X': Fore.RED,
            'O': Fore.GREEN,
            '-': Fore.WHITE,
            '#': Fore.YELLOW,
            '@': Fore.CYAN,
            '*': Fore.MAGENTA,
            '+': Fore.BLUE
        }
        
        # Define block character mappings for better visualization
        self.block_chars = {
            'X': '█',
            'O': '█',
            '-': '·',
            '#': '█',
            '@': '█',
            '*': '█',
            '+': '█'
        }
        
        # Define emoji mappings for fun visualization
        self.emoji_chars = {
            'X': '🟥',
            'O': '🟩',
            '-': '⬜',
            '#': '🟨',
            '@': '🟦',
            '*': '🟪',
            '+': '🟫'
        }
    
    def print_grid(self, grid):
        """
        Print the grid in plain text format.
        
        Args:
            grid (List[List[str]]): The 2D grid to display
        """
        for row in grid:
            print(" ".join(str(cell) for cell in row))
        print()
    
    def print_colored_grid(self, grid):
        """
        Print the grid with color coding for better visualization.
        
        Args:
            grid (List[List[str]]): The 2D grid to display
        """
        for row in grid:
            for cell in row:
                # Get the color for this cell (default to white)
                color = self.colors.get(cell, Fore.WHITE)
                
                # Determine which character to display
                if self.use_emojis:
                    display_char = self.emoji_chars.get(cell, cell)
                    print(display_char, end=" ")
                elif self.use_blocks:
                    display_char = self.block_chars.get(cell, cell)
                    print(color + display_char + Style.RESET_ALL, end=" ")
                else:
                    print(color + cell + Style.RESET_ALL, end=" ")
            print()
        print()
    
    def animate_fill(self, grid, delay=0.05):
        """
        Display the grid with a slight delay for animation effect.
        
        Args:
            grid (List[List[str]]): The 2D grid to display
            delay (float): Time delay in seconds between frames
        """
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Display the grid
        self.print_colored_grid(grid)
        
        # Wait before the next frame
        time.sleep(delay)
    
    def display_stats(self, stats):
        """
        Display statistics about the flood fill operation.
        
        Args:
            stats (dict): Dictionary containing statistics
        """
        print(Fore.CYAN + "Flood Fill Statistics:" + Style.RESET_ALL)
        print(f"Cells filled: {stats['cells_filled']}")
        print(f"Time taken: {stats['time_taken']:.4f} seconds")
        print(f"Fill rate: {stats['cells_filled'] / stats['time_taken']:.2f} cells/second")
        print()