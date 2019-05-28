import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("brown")
        self.penup()
        self.speed(0)

class Player (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Tresure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create levels list
levels = [""]

#Define first level-
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXX          XXXXXX",
"X  XXXXXX  XXXXXX  XXXXXX",
"X      XX  XXXXXX  XXXXXX",
"X      XX  XXX         XX",
"XXXXX  XX  XXX         XX",
"XXXXX  XX  XXXXXX  XXXXXX",
"XXXXX  XX    XXXX  XXXXXX",
"X  XX        XXXX  XXXXXX",
"X  XX  XXXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXXX",
"X               XXXXXXXXX",
"XXXXXXXXXX      XXXXX   X",
"XXXXXXXXXXXXX   XXXXX   X",
"XXX  XXXXXXXX           X",
"XXX                     X",
"XXX       XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX                X",
"XX XXXX       T         X",
"XX  XXXXXXXXXXX    XXXXXX",
"XX   YXXXXXXXXX         X",
"XX        XXXX          X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
 ]

#Add a treasures list
treasures = []

#Add maze to mazes list
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in  range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representinga wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))

            #Check if it is a P (repensenting the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing the Treasure)
            if character == "T":
                treasures.append(Tresure(screen_x, screen_y))

#Create class instances
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []

#Set up the level
setup_maze(levels[1])
print(walls)

#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"d")
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"s")

#Turn off screen updates
wn.tracer(0)

#Main Game loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasure list
            treasures.remove(treasure)


    #Update screen
    wn.update()

