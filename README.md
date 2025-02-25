# Flood Fill Algorithm Using BFS 🎨
<p align="center">
  <img src="https://i0.wp.com/www.techiedelight.com/wp-content/uploads/Flood-Fill.png?resize=504%2C222&ssl=1" alt="Flood Fill Example">
</p>

This repository demonstrates the **Flood Fill Algorithm** using **Breadth-First Search (BFS)** in Python.  The implementation provides an interactive command-line interface for running the algorithm on example grids or custom grids. 🚀

## Features
- BFS-based flood fill implementation
- Interactive CLI for selecting grids and configuring fill parameters
- Visualization of the fill process ✨
- Example grids for quick testing 🧪
- Custom grid creation option 📝

## Repository Structure
```
.
├── LICENSE             # License file
├── README.md           # Project documentation
├── requirements.txt    # Dependencies required to run the project
├── examples.py         # Example grids for testing
├── floodfill.py        # BFS flood fill implementation
├── main.py             # Main interactive CLI for running the algorithm
├── visualizer.py       # Grid visualization module

```

## Installation & Setup
### Prerequisites
Ensure you have Python 3 installed on your system.  It's recommended to use a virtual environment for project isolation. 🐍

### Steps
1. Clone the repository:
   ```bash
   git clone [<repository_url>](https://github.com/imaddde867/BFS-Floodfill.git)
   cd BFS-App
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
Execute the following command to launch the interactive demo:
```bash
python main.py
```

Follow the on-screen prompts to select an example grid, create a custom one, configure fill parameters, and watch the algorithm in action! 🎬

## Usage
1. Choose an example grid or craft your own custom grid. 🗺️
2. Select the starting point for the flood fill operation.  Click on the starting cell. 🖱️
3. Choose a fill character.  Select a color or symbol to fill with.  🎨
4. Optionally enable animation for a visual walkthrough.  Enable animation for a visual treat! ✨
5. Observe the filled grid and performance statistics.  Check out the results and timings! 📊

## Example Output
```
============================================================
Flood Fill Algorithm Demonstration 🚀
============================================================

This program demonstrates the flood fill algorithm using BFS.
It's similar to the 'paint bucket' tool in graphic editors.  🪣

Choose an example grid or create your own:
1. Use an example grid
2. Create a custom grid
...
Performing flood fill...
Final Result:
[Grid output with filled areas]
```

## Future Improvements
- Implement Depth-First Search (DFS) as an alternative algorithm. 🔄
- Add graphical visualization using Tkinter or Pygame for a more immersive experience.  🎮
- Enhance user experience with a more intuitive UI and better error handling.  👍

## License
This project is licensed under the terms of the [MIT License](LICENSE).  📜
