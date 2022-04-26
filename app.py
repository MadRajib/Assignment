import turtle

WIN_WIDTH = 500
WIN_HEIGHT = 500
INPUT_RANGE = (0,20)

home_x = None
home_y = None
points = None
x_tick_len = None
y_tick_len = None
prev_pt = None

def init(x, y):
    global home_x
    global home_y
    global points
    global x_tick_len
    global y_tick_len
    global prev_pt
    home_x = x
    home_y = y
    points = []
    x_tick_len = 10
    y_tick_len = 40
    prev_pt = (home_x,home_y)

def go_home(trtl):
    trtl.up()
    trtl.goto(home_x,home_y)

def draw_ticks(trtl, dir, tick_len = 10, val = 0):

    if(dir == "up"):
        trtl.left(90)
            
    elif(dir == "right"):
        trtl.left(90)

    trtl.down()
    trtl.forward(tick_len)
    trtl.write(val)
    trtl.backward(2*tick_len)
    trtl.up()
    trtl.forward(tick_len)
    trtl.right(90)

def draw_axis(trtl , pts):
    global x_tick_len
    global y_tick_len
    x_tick_len = int((WIN_WIDTH - 100) /(pts + 1))
    y_tick_len = int((WIN_HEIGHT -100) / 6)
    go_home(trtl)

        # Y axis
    trtl.left(90)
    trtl.up()

    for tks in range(INPUT_RANGE[0]+ 4,INPUT_RANGE[1] + 4, 4):
        trtl.down()
        trtl.forward(y_tick_len)
        draw_ticks(trtl, "up", val = tks)
        trtl.up()
    
    trtl.shape("arrow")
    trtl.down()
    trtl.forward(y_tick_len)
    trtl.stamp()
    trtl.up()

    go_home(trtl)
    trtl.right(90)
        
    print(pts)
    for tks in range(1, pts + 1):
        trtl.down()
        trtl.forward(x_tick_len)
        draw_ticks(trtl, "right", val = tks)
        trtl.up()

    trtl.down()
    trtl.forward(x_tick_len)
    trtl.stamp()
    trtl.up()
    trtl.shape("square")

def plot_point(trtl, pt = (0,0)):
    global prev_pt
    go_home(trtl)
    x_pos = home_x + (pt[0]*x_tick_len)
    y_pos = home_y + (pt[1]/4)*y_tick_len

    print(pt, x_pos,y_pos)
    trtl.goto(x_pos, y_pos)
    trtl.down()
    trtl.turtlesize(stretch_wid = 0.3 , stretch_len = 0.3)
    trtl.color("red")
    trtl.stamp()
    trtl.up()
    draw_line(trtl, (x_pos, y_pos))
    prev_pt = (x_pos, y_pos)

def draw_line(trtl, pt= (0,0)):
    trtl.up()
    if(prev_pt != (home_x,home_y)) :
        trtl.goto(prev_pt[0],prev_pt[1])
    trtl.down()
    trtl.goto(pt[0],pt[1])
    trtl.up()


screen = turtle.Screen()
trl = turtle.Turtle()

trl.speed('fastest')
trl.shape("square")
trl.hideturtle()

screen.setup(WIN_WIDTH,WIN_HEIGHT)

# initialize global vars
init( -200, -200)
num_pts = None

# take number of points
while (num_pts == None) : 
    num_pts = screen.numinput("Number of Points", "Points:", 0, minval = INPUT_RANGE[0], maxval = INPUT_RANGE[1])
    if (num_pts == None):
        print(f"Please enter a valid number of points in range {INPUT_RANGE}")

num_pts = int(num_pts)

# draw axis based on the points
draw_axis(trl, num_pts)

# take point as input from user and plot the point
for i in range(num_pts) :
    pt = screen.numinput(f"Point {i+1}", "Val:", 0, minval = INPUT_RANGE[0], maxval = INPUT_RANGE[1])
    if (pt != None):
        plot_point(trl, (i+1,pt))

screen.exitonclick()


