import tkinter as tk
from tkinter import messagebox
import random
from collections import deque

# Create a random maze (0 = path, 1 = wall)
def make_maze(rows, cols, wall_chance=0.3):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < wall_chance:
                row.append(1)  # wall
            else:
                row.append(0)  # path
        maze.append(row)
    return maze

# BFS for shortest path
def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    q = deque([start])
    parent = {start: None}
    seen = {start}

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        r, c = q.popleft()

        if (r, c) == end:
            break

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    q.append((nr, nc))

    if end not in parent:
        return None

    path = []
    cur = end
    while cur:
        path.append(cur)
        cur = parent[cur]

    return path[::-1]

# Tkinter GUI
class MazeApp:
    def __init__(self, root):
        self.rows = 8
        self.cols = 8
        self.cell_size = 40

        self.root = root
        self.root.title(f"BFS Maze Pathfinding - {self.rows} Rows x {self.cols} Columns")

        self.maze = make_maze(self.rows, self.cols)
        self.start = None
        self.end = None

        # GUI setup
        self.canvas = tk.Canvas(root, width=self.cols*self.cell_size,
                                height=self.rows*self.cell_size, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4, pady=10)
        self.canvas.bind("<Button-1>", self.on_click)

        # Labels
        tk.Label(root, text="Click a cell to set: Start (blue), End (red), Wall (black)").grid(row=1, column=0, columnspan=4)
        
        # Buttons
        tk.Button(root, text="Generate Maze", command=self.generate_maze).grid(row=2, column=0)
        tk.Button(root, text="Find Path", command=self.find_path).grid(row=2, column=1)
        tk.Button(root, text="Reset Start/End", command=self.reset_start_end).grid(row=2, column=2)
        tk.Button(root, text="Clear Walls", command=self.clear_walls).grid(row=2, column=3)

        # Draw legend
        self.draw_legend()
        self.draw_maze()

    # Draw maze grid
    def draw_maze(self, path=None):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Set color
                if self.maze[r][c] == 1:
                    color = "black"  # wall
                else:
                    color = "white"  # path

                if self.start == (r,c):
                    color = "blue"   # start
                elif self.end == (r,c):
                    color = "red"    # end
                elif path and (r,c) in path:
                    color = "lightgreen"  # BFS path

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    # Draw color legend
    def draw_legend(self):
        legend_frame = tk.Frame(self.root)
        legend_frame.grid(row=3, column=0, columnspan=4)
        colors = [("White", "Path"), ("Black", "Wall"), ("Blue", "Start"), ("Red", "End"), ("LightGreen", "BFS Path")]
        for i, (color, text) in enumerate(colors):
            tk.Label(legend_frame, text="   ", bg=color).grid(row=0, column=i*2)
            tk.Label(legend_frame, text=text).grid(row=0, column=i*2+1)

    # Mouse click on canvas
    def on_click(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # Set start if not set
            if not self.start:
                self.start = (row, col)
            # Set end if start is set and end not set
            elif not self.end:
                self.end = (row, col)
            # Otherwise toggle wall
            else:
                if (row, col) != self.start and (row, col) != self.end:
                    self.maze[row][col] = 1 if self.maze[row][col] == 0 else 0
            self.draw_maze()

    # Generate new maze
    def generate_maze(self):
        self.maze = make_maze(self.rows, self.cols)
        self.start = None
        self.end = None
        self.draw_maze()

    # Reset start/end
    def reset_start_end(self):
        self.start = None
        self.end = None
        self.draw_maze()

    # Clear all walls
    def clear_walls(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.maze[r][c] = 0
        self.draw_maze()

    # Find BFS path
    def find_path(self):
        if not self.start or not self.end:
            messagebox.showerror("Error", "Please set start and end positions")
            return
        if self.maze[self.start[0]][self.start[1]] == 1 or self.maze[self.end[0]][self.end[1]] == 1:
            messagebox.showerror("Error", "Start or end is on a wall!")
            return
        path = bfs(self.maze, self.start, self.end)
        if not path:
            messagebox.showinfo("Result", "No path found")
        else:
            messagebox.showinfo("Result", f"Path found! Steps: {len(path)-1}")
        self.draw_maze(path)

# Run App
root = tk.Tk()
MazeApp(root)
root.mainloop()