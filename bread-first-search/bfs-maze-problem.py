import turtle
import sys
from collections import deque


myScreen = turtle.Screen()      # Define the turtle screen
myScreen.bgcolor('black')       # setup background color

myScreen.title("BFS for find path from START to END")

myScreen.setup(1300, 700)       # Setup the dimessions of the working window

# This is the class for the Maze walls


class Maze(turtle.Turtle):  # Inherant from turtle.Turtle class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # setup turtle shape
        self.color("white")  # setup turle color
        self.penup()            # lift up the pen so it do not leave a trail
        self.speed(0)
        self.hideturtle()

# Create Yellow class for the finish line (from starting point to ending point)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('turtle')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.hideturtle()

# class Red for Starting Location


class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('red')
        self.penup()
        self.speed(0)
        self.hideturtle()
# Class purple for ending location


class Purple(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('purple')
        self.penup()
        self.speed(0)
        self.hideturtle()

# Class blue for all posible move


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.hideturtle()


grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++                 +++++++  ++++++++++++",
    "+s         e+                 +               ++  +",
    "+  +++++++                                        +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +                 +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +        +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++           +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +             +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +              ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+        ++++++              ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++      +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     +     +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++        ++++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

# Set up maze


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x*24)
            screen_y = 288 - (y*24)
            cell = (screen_x, screen_y)
            if character == '+':
                # move pen to the x,y location
                maze.goto(screen_x, screen_y)
                maze.stamp()                            # and stamp a copy of the turtle on the screen
                walls.append(cell)      # add coordinate to walls list

            if character == 's':
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)
                red.stamp()
            if character == 'e':
                end_x, end_y = screen_x, screen_y
                purple.goto(screen_x, screen_y)
                purple.stamp()

            if character == ' ' or character == 'e':
                path.append(cell)

# main algorithm search from starting location (x,y) for ending location(end_x, end_y)


def bfs_search(x, y):
    frontier.append((x, y))          # Create a queue with starting location
    solution[x, y] = (x, y)

    while len(frontier) > 0:
        # current cell
        (x, y) = frontier.popleft()

        if (x, y) == (end_x, end_y):
            break
        direction = [(-24, 0), (24, 0), (0, 24), (0, -24)]
        for i in range(len(direction)):
            cell = (x+direction[i][0], y+direction[i][1])
            if cell in path and cell not in visited:    # check if the cell is in path and not in visited
                solution[cell] = (x, y)
                frontier.append(cell)
                visited.add(cell)
            if (x, y) != (start_x, start_y):
                blue.goto(x, y)
                blue.stamp()


def backRouting(x, y):
    (x, y) = solution[x, y]
    while (x, y) != (start_x, start_y):
        yellow.goto(x, y)
        yellow.stamp()
        (x, y) = solution[(x, y)]


# Create instances from class
maze = Maze()
red = Red()
purple = Purple()
blue = Blue()
yellow = Yellow()

# Create some variable
path = []               # Store all posible moves
visited = set()         # Store visited cell
walls = []              # Store wall cell
frontier = deque()
# Store {(x,y) : (prev_x, prev_y)} pairs for backtracking
solution = {}

setup_maze(grid)
bfs_search(start_x, start_y)
backRouting(end_x, end_y)

myScreen.exitonclick()
