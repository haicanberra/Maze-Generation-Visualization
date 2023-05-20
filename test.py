import pygame
import sys

# Set the dimensions of the grid
GRID_SIZE = 20
GRID_WIDTH = 40
GRID_HEIGHT = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
clock = pygame.time.Clock()

# Create a 2D array to represent the grid
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Set the start and end points
start = (0, 0)
end = (GRID_HEIGHT - 1, GRID_WIDTH - 1)

# Create a stack to store the path
stack = [start]

# Run the depth-first search algorithm
while stack:
    current = stack.pop()
    x, y = current

    if grid[x][y] == 1:
        continue

    grid[x][y] = 1

    if current == end:
        break

    # Check the neighbors
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for neighbor in neighbors:
        nx, ny = neighbor
        if 0 <= nx < GRID_HEIGHT and 0 <= ny < GRID_WIDTH and grid[nx][ny] != 1:
            stack.append(neighbor)

# Set up the display
screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE
            if grid[row][col] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the start and end points
    pygame.draw.rect(screen, RED, (start[1] * GRID_SIZE, start[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (end[1] * GRID_SIZE, end[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
    pygame

# Quit the game
pygame.quit()
sys.exit()
