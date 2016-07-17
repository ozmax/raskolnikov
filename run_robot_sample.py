import random
import time

from maze import MAZES, WALLS, GOALS, BLANKS
from Navigation import DFS, BFS
from Robot import Robot

maze = random.choice(MAZES)
nav_system = random.choice([DFS, BFS])

robot = Robot(
    maze,
    BLANKS,
    WALLS,
    GOALS,
    initial_pos=(6, 1),
    Navigation=nav_system
)

robot.get_path()
while robot.navigation.has_next_move():
    robot.move()
    data = robot.print_current_pos()
    with open('data.txt', 'r+b') as f:
        f.write(data)
        f.write('using %s nav system' % nav_system.__name__)
    time.sleep(0.1)
