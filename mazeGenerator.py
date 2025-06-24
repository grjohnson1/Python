import pygame
import random
import sys

# Configuration
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

# Directions: Top, Right, Bottom, Left
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.visited = False
        self.walls = [True, True, True, True]

    def draw(self):
        x = self.x * CELL_SIZE
        y = self.y * CELL_SIZE
        if self.visited:
            pygame.draw.rect(screen, (40, 40, 40), (x, y, CELL_SIZE, CELL_SIZE))
        if self.walls[0]:
            pygame.draw.line(screen, pygame.Color("white"), (x, y), (x + CELL_SIZE, y))
        if self.walls[1]:
            pygame.draw.line(screen, pygame.Color("white"), (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
        if self.walls[2]:
            pygame.draw.line(screen, pygame.Color("white"), (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))
        if self.walls[3]:
            pygame.draw.line(screen, pygame.Color("white"), (x, y + CELL_SIZE), (x, y))

def index(x, y):
    if 0 <= x < COLS and 0 <= y < ROWS:
        return y * COLS + x
    return None

# Maze setup
grid = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
stack = []
current = grid[0]

def remove_walls(a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    if dx == 1: a.walls[1] = False; b.walls[3] = False
    if dx == -1: a.walls[3] = False; b.walls[1] = False
    if dy == 1: a.walls[2] = False; b.walls[0] = False
    if dy == -1: a.walls[0] = False; b.walls[2] = False

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    for cell in grid:
        cell.draw()

    # Draw start (green) and finish (red)
    start_x = CELL_SIZE // 2
    start_y = CELL_SIZE // 2
    pygame.draw.circle(screen, (0, 255, 0), (start_x, start_y), CELL_SIZE // 4)

    end_x = (COLS - 1) * CELL_SIZE + CELL_SIZE // 2
    end_y = (ROWS - 1) * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, (255, 0, 0), (end_x, end_y), CELL_SIZE // 4)

    current.visited = True
    neighbors = []
    for dx, dy in DIRS:
        i = index(current.x + dx, current.y + dy)
        if i is not None and not grid[i].visited:
            neighbors.append(grid[i])
    if neighbors:
        next_cell = random.choice(neighbors)
        stack.append(current)
        remove_walls(current, next_cell)
        current = next_cell
    elif stack:
        current = stack.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
