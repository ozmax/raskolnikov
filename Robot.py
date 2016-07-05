from maze import MAZE, BLANKS, WALLS


def normalize_maze(maze):
    norm_maze = []
    for line in MAZE:
        new_line = [char for char in line]
        norm_maze.append(new_line)
    return norm_maze

maze = normalize_maze(MAZE)


class Robot(object):

    visited_places = []

    def __init__(self, maze, spaces, walls, initial_pos):
        self.maze = maze
        self.spaces = spaces
        self.walls = walls
        if maze[initial_pos[0]][initial_pos[1]] in walls:
            raise Exception("Starting position is on a wall")
        else:
            self.current_pos = initial_pos

    def choices(self):
        pass

    def random_picker(self, choices):
        pass

    def pretify_maze(self, maze):
        pmaze = ''
        for line in maze:
            pline = ''.join(line)
            pline += '\n'
            pmaze += pline
        return pmaze

    def print_current(self):
        maze = self.maze
        maze[self.current_pos[0]][self.current_pos[1]] = 'X'
        maze = self.pretify_maze(maze)
        print maze


robot = Robot(maze=maze, spaces=BLANKS, walls=WALLS, initial_pos=(7, 25))
print robot.maze
