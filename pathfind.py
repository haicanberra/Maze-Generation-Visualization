def get_algo_string(algorithm):
    match algorithm:
        case "DFS":
            return "DFS"
        case "BFS":
            return "BFS"
        case "ASTAR":
            return "A Star"
        case "DIJ":
            return "Dijkstra"
def pathfind(algorithm, grid_class, start_pos, end_pos):
    match algorithm:
        case "DFS":
            return depth_first_search(grid_class, start_pos, end_pos)
        case "BFS":
            return breadth_first_search(grid_class, start_pos, end_pos)
        case "ASTAR":
            return a_star_search(grid_class, start_pos, end_pos)
        case "DIJ":
            return dijkstra_search(grid_class, start_pos, end_pos)

def depth_first_search(grid_class, start_pos, end_pos):
    (grid_class.get_grid())[start_pos[0]][start_pos[1]].set_found()
    if start_pos == end_pos:
        return True

    walls = (grid_class.get_grid())[start_pos[0]][start_pos[1]].get_wall()
    neighbors = (grid_class.get_neighbors())[start_pos]
    for i in range(4):
        if not walls[i]:
            if neighbors[i] != None:
                next_pos = neighbors[i]
                if not (grid_class.get_grid())[next_pos[0]][next_pos[1]].get_found():
                    if depth_first_search(grid_class, next_pos, end_pos):
                        (grid_class.get_grid())[next_pos[0]][next_pos[1]].set_path()
                        return True

    return False

def breadth_first_search(grid_class, start_pos, end_pos):
    grid = grid_class.get_grid()
    grid[start_pos[0]][start_pos[1]].set_found()

    if start_pos == end_pos:
        grid[start_pos[0]][start_pos[1]].set_path()
        return True

    queue = [start_pos]
    front = 0

    parents = {start_pos: None}  # Initialize the parents dictionary

    while front < len(queue):
        current_pos = queue[front]
        front += 1

        walls = grid[current_pos[0]][current_pos[1]].get_wall()
        neighbors = grid_class.get_neighbors()[current_pos]

        for i in range(4):
            if not walls[i]:
                if neighbors[i] is not None:
                    next_pos = neighbors[i]
                    if not grid[next_pos[0]][next_pos[1]].get_found():
                        grid[next_pos[0]][next_pos[1]].set_found()
                        queue.append(next_pos)
                        parents[next_pos] = current_pos  # Update the parent of next_pos
                        if next_pos == end_pos:
                            # Mark the path from start to goal
                            path_pos = end_pos
                            while path_pos is not None:
                                grid[path_pos[0]][path_pos[1]].set_path()
                                path_pos = parents[path_pos]
                            return True

    return False

def heuristic(position, end_pos):
    # Calculate the Manhattan distance heuristic between two positions
    return abs(position[0] - end_pos[0]) + abs(position[1] - end_pos[1])

def a_star_search(grid_class, start_pos, end_pos):
    grid = grid_class.get_grid()
    grid[start_pos[0]][start_pos[1]].set_found()

    if start_pos == end_pos:
        grid[start_pos[0]][start_pos[1]].set_path()
        return True

    open_set = [start_pos]  # Store the positions to be evaluated
    parents = {start_pos: None}  # Store the parent of each visited position
    g_scores = {start_pos: 0}  # Store the g-score for each visited position

    while open_set:
        # Find the position with the lowest f-score in the open set
        current_pos = min(open_set, key=lambda pos: g_scores[pos] + heuristic(pos, end_pos))

        if current_pos == end_pos:
            # Mark the path from start to goal
            path_pos = end_pos
            while path_pos is not None:
                grid[path_pos[0]][path_pos[1]].set_path()
                path_pos = parents[path_pos]
            return True

        open_set.remove(current_pos)
        grid[current_pos[0]][current_pos[1]].set_found()  # Set the current cell as found

        walls = grid[current_pos[0]][current_pos[1]].get_wall()
        neighbors = grid_class.get_neighbors()[current_pos]

        for i in range(4):
            if not walls[i]:
                if neighbors[i] is not None:
                    next_pos = neighbors[i]
                    tentative_g_score = g_scores[current_pos] + 1

                    if next_pos not in g_scores or tentative_g_score < g_scores[next_pos]:
                        g_scores[next_pos] = tentative_g_score
                        parents[next_pos] = current_pos

                        if next_pos not in open_set:
                            open_set.append(next_pos)

    return False

def dijkstra_search(grid_class, start_pos, end_pos):
    grid = grid_class.get_grid()
    grid[start_pos[0]][start_pos[1]].set_found()

    if start_pos == end_pos:
        grid[start_pos[0]][start_pos[1]].set_path()
        return True

    queue = [(0, start_pos)]  # Use a list as a priority queue to store positions with their corresponding costs
    parents = {start_pos: None}  # Store the parent of each visited position
    costs = {start_pos: 0}  # Store the cost for each visited position

    while queue:
        queue.sort(key=lambda x: x[0])
        _, current_pos = queue.pop(0)

        if current_pos == end_pos:
            # Mark the path from start to goal
            path_pos = end_pos
            while path_pos is not None:
                grid[path_pos[0]][path_pos[1]].set_path()
                path_pos = parents[path_pos]
            return True

        walls = grid[current_pos[0]][current_pos[1]].get_wall()
        neighbors = grid_class.get_neighbors()[current_pos]

        for i in range(4):
            if not walls[i]:
                if neighbors[i] is not None:
                    next_pos = neighbors[i]
                    cost = costs[current_pos] + 1

                    if next_pos not in costs or cost < costs[next_pos]:
                        costs[next_pos] = cost
                        parents[next_pos] = current_pos

                        queue.append((cost, next_pos))
                        grid[next_pos[0]][next_pos[1]].set_found()

    return False







