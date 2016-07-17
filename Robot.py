class Robot(object):

    def __init__(self, maze, spaces, walls, goal, initial_pos,  Navigation):

        def normalize_maze(maze):
            norm_maze = []
            for line in maze:
                new_line = [char for char in line]
                norm_maze.append(new_line)
            return norm_maze

        maze = normalize_maze(maze)
        self.navigation = Navigation(maze, spaces, walls, goal, initial_pos)
        self.maze = maze
        self.current_pos = initial_pos

    def print_pretty(self, maze):
        pmaze = ''
        for line in maze:
            pline = ''.join(line)
            pline += '\n'
            pmaze += pline
        return pmaze

    def get_path(self):
        path = self.navigation.calculate_path()

        return path

    def move(self):
        move = self.navigation.get_next_move()
        self.maze[self.current_pos[0]][self.current_pos[1]] = ' '
        self.current_pos = move
        self.maze[move[0]][move[1]] = 'X'

    def print_current_pos(self):
        return self.print_pretty(self.maze)
