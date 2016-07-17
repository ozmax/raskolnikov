class NavigationBase(object):

    def __init__(self, maze, spaces, walls, goal, initial_pos):

        self.maze = maze
        self.spaces = spaces
        self.walls = walls
        self.goal = goal

        if maze[initial_pos[0]][initial_pos[1]] in walls:
            raise Exception("Starting position is on a wall")
        else:
            self.current_pos = initial_pos
            self.initial_pos = initial_pos

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

    def calculate_path(self):
        raise NotImplemented

    def has_next_move(self):
        if self.path:
            return True

    def get_next_move(self):
        if self.path:
            return self.path.pop(0)
        else:
            return None

    def print_pretty(self, maze):
        pmaze = ''
        for line in maze:
            pline = ''.join(line)
            pline += '\n'
            pmaze += pline
        return pmaze


class DFS(NavigationBase):
    stack = []
    visited = []

    def get_adjacent_unvisited(self):
        unvisited = []
        choices = self.get_choices()
        for key, value in choices.iteritems():
            if value not in self.visited:
                unvisited.append(value)
        return unvisited

    def calculate_path(self):
        self.stack.append(self.current_pos)
        self.visited.append(self.current_pos)
        while self.stack:
            if self.maze[self.current_pos[0]][self.current_pos[1]] in self.goal:
                break
            children = self.get_adjacent_unvisited()
            if children:
                self.current_pos = children[0] # random.choice(children)
                self.visited.append(self.current_pos)
                self.stack.append(self.current_pos)
            else:
                self.stack.pop()
                self.current_pos = self.stack[-1]

        self.path = self.stack
        return self.stack


class BFS(NavigationBase):
    visited = set()

    def get_adjacent_unvisited(self):
        unvisited = []
        choices = self.get_choices()
        for key, value in choices.iteritems():
            if value not in self.visited and value not in self.queue:
                unvisited.append(value)
        return unvisited

    def children_with_parent(self, children, parent):
        return {child: parent for child in children}

    def calculate_path(self):
        history = {}
        self.queue = [self.current_pos]

        while self.queue:
            self.current_pos = self.queue.pop(0)
            self.visited.add(self.current_pos)

            if self.maze[self.current_pos[0]][self.current_pos[1]] in self.goal:
                break

            ch = self.get_adjacent_unvisited()
            self.queue += ch
            history.update(self.children_with_parent(ch, self.current_pos))

        pointer = self.current_pos
        path = []
        while pointer != self.initial_pos:
            pointer = history[pointer]
            path.append(pointer)
        path.reverse()

        self.path = path
        return path
