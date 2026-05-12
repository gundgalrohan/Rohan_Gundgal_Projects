BFS Maze Pathfinder
A visual maze pathfinding application built with Python and Tkinter that uses Breadth-First Search (BFS) to find the shortest path between two points.
Features

Random maze generation with configurable wall density
Interactive grid: click to set Start, End, and toggle walls
BFS shortest path visualization in real-time
Controls: Generate Maze, Find Path, Reset Start/End, Clear Walls

Tech Stack
Python Tkinter BFS Collections.deque

How to Run
bashpip install tk
python bfs_maze.py

Usage
Click a cell → sets Start (blue)
Click another → sets End (red)
Click remaining cells → toggles walls
Hit Find Path to run BFS and see the green shortest path
