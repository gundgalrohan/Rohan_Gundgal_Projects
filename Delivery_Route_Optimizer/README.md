Delivery Route Optimizer
A C++ console application that optimizes delivery routes using the Bellman-Ford shortest path algorithm, maximizing profit within distance constraints.

Features
Add/delete roads with distances between locations
Add/delete delivery tasks with profit values
Greedy optimizer: picks highest-profit deliveries within a max distance budget
Multi-stop route planning from a chosen starting location

Tech Stack
C++ Bellman-Ford Algorithm Greedy Strategy STL

How to Compile & Run
bashg++ delivery_optimizer.cpp -o optimizer
./optimizer

Usage\
Enter number of places (labeled A, B, C...)
Add roads and deliveries via the menu
Run the optimizer with a start point, max deliveries, and max distance
