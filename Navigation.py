class NavigationBase(object):

    def __init__(self, maze, spaces, walls, goal, initial_pos):
        self.maze = maze
        self.spaces = spaces
        self.walls = walls
        if maze[initial_pos[0]][initial_pos[1]] in walls:
            raise Exception("Starting position is on a wall")
        else:
            self.current_pos = initial_pos

    def get_choices(self):
        choices = {}
        # move left
        if ((self.current_pos[1] - 1) >= 0):
            if self.maze[self.current_pos[0]][self.current_pos[1] - 1] \
                    not in self.walls:
                left = (self.current_pos[0], self.current_pos[1] - 1)
                choices['left'] = left
        # move right
        if ((self.current_pos[1] + 1) <= len(self.maze[0]) - 1):
            if self.maze[self.current_pos[0]][self.current_pos[1] + 1] \
                     not in self.walls:
                right = (self.current_pos[0], self.current_pos[1] + 1)
                choices['right'] = right
        # move up
        if ((self.current_pos[0] - 1) >= 0):
            if self.maze[self.current_pos[0] - 1][self.current_pos[1]] \
                    not in self.walls:
                up = (self.current_pos[0] - 1, self.current_pos[1])
                choices['up'] = up
        # move down
        if ((self.current_pos[0] + 1) <= len(self.maze) - 1):
            if self.maze[self.current_pos[0] + 1][self.current_pos[1]]\
                    not in self.walls:
                down = (self.current_pos[0] + 1, self.current_pos[1])
                choices['down'] = down

        return choices

    def get_next_move(self):
        raise NotImplemented

    def move(self):
        raise NotImplemented


class OneDirection(NavigationBase):
    """ Change direction when bump on obstacle"""
    last_direction = None

    def first_move(self):
        """" first move is random """
        choices = self.get_choices()
        import random
        choice = random.choice(choices.keys())
        return choice, choices[choice]

    def move(self):
        if self.last_direction is None:
            choice_name, choice = self.first_move()
            self.last_direction = choice_name
        choices = self.get_choices()
        if self.last_direction in choices:
            choice = choices[self.last_direction]
        if self.last_direction not in choices:
            import random
            choice_name = random.choice(choices.keys())
            choice = choices[choice_name]
            self.last_direction = choice_name
        self.current_pos = choice
        return choice
