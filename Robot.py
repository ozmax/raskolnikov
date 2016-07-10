import copy


class Robot(object):

    def __init__(self, maze, spaces, walls, goal, initial_pos,  Navigation):

        self.navigation = Navigation(maze, spaces, walls, goal, initial_pos)

    def print_pretty(self, maze):
        pmaze = ''
        for line in maze:
            pline = ''.join(line)
            pline += '\n'
            pmaze += pline
        return pmaze

    def move(self):
        # choice = self.get_random(self.get_choices())
        new_position = self.navigation.move()
        self.current_pos = new_position

    def get_current(self):
        maze = copy.deepcopy(self.navigation.maze)
        maze[self.navigation.current_pos[0]][self.navigation.current_pos[1]]\
            = 'X'
        return self.print_pretty(maze)
