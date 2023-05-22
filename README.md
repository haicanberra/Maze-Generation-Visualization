# Pathfinding Algorithms Visualization

## About
A visualization tool written in Python using Pygame for visualizing pathfinding algorithms in randomly generated mazes.

## Packages
Pygame.

## References
None.

## Mathematics
Iterative randomized depth-first search is used for maze generation.  
  
The neighbor priority used: Left - Top - Right - Bottom.  
  
Algorithms included:  
1. Depth-first Search  
    Explores as far as possible along each branch path before backtracking. Uses stack to store cells discovered for backtracking.
2. Breadth-first Search  
    Explores all cells at the present depth prior to moving on to the cells at the next depth level. Uses queue to store cells found but not explored.
3. Dijkstra's Algorithm  
    Iteratively explore cheapest cost cells with the cost being the steps to reach that cell. Uses a queue with cost included.
4. A* Algorithm  
    Dijkstra's Algorithm but with heuristic using Manhattan distance. The score of each cell is the sum of the cost and heuristic.
## Notes
- Click Start/End to set start/end cells.
- Regen for regenerating the maze.
- Clear to clear the paths but retain the maze.
## Installation
```
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
```  
## Futher Optimizations:
- Selections of maze generating algorithms.
- Maybe more pathfinding algorithms.


