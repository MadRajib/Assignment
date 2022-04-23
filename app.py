import turtle

WIN_WIDTH = 500
WIN_HEIGHT = 500
INPUT_RANGE = (0,20)


class Graph:
    def __init__(self, home_x, home_y):
        self.home_x = home_x
        self.home_y = home_y
        self.points = []
        self.x_tick_len = 10
        self.y_tick_len = 40
        self.prev_pt = (self.home_x,self.home_y)

    def go_home(self, trtl):
        trtl.up()
        trtl.goto(self.home_x,self.home_y)

    def draw_ticks(self,trtl, dir, tick_len = 10, val = 0):

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

    def draw_axis(self, trtl , pts):
        self.go_home(trtl)

        # Y axis
        trtl.left(90)
        trtl.up()

        for tks in range(INPUT_RANGE[0]+ 4,INPUT_RANGE[1] + 4, 4):
            trtl.down()
            trtl.forward(self.y_tick_len)
            self.draw_ticks(trtl, "up", val = tks)
            trtl.up()

        self.go_home(trtl)
        trtl.right(90)
        
        print(pts)
        for tks in range(1, pts + 1):
            trtl.down()
            trtl.forward(self.x_tick_len)
            self.draw_ticks(trtl, "right", tick_len = self.x_tick_len, val = tks)
            trtl.up()
        trtl.down()
        trtl.forward(self.x_tick_len)
        trtl.up()

    def plot_point(self, trtl, pt = (0,0)):
        self.go_home(trtl)
        x_pos = self.home_x + (pt[0]*self.x_tick_len)
        y_pos = self.home_y + (pt[1]/4)*self.y_tick_len

        print(pt, x_pos,y_pos)
        trtl.goto(x_pos, y_pos)
        trtl.down()
        trtl.dot()
        trtl.up()
        self.draw_line(trtl, (x_pos, y_pos))
        self.prev_pt = (x_pos, y_pos)

    def draw_line(self,trtl, pt= (0,0)):
        trtl.up()
        trtl.goto(self.prev_pt[0],self.prev_pt[1])
        trtl.down()
        trtl.goto(pt[0],pt[1])
        trtl.up()


screen = turtle.Screen()
trl = turtle.Turtle()

trl.speed('fastest')
trl.hideturtle()

screen.setup(WIN_WIDTH,WIN_HEIGHT)

graph = Graph( -200, -200)
num_pts = None
while (num_pts == None) : 
    num_pts = screen.numinput("Number of Points", "Points:", 0, minval = INPUT_RANGE[0], maxval = INPUT_RANGE[1])
    if (num_pts == None):
        print(f"Please enter a valid number of points in range {INPUT_RANGE}")

num_pts = int(num_pts)
graph.draw_axis(trl, num_pts)
for i in range(num_pts) :
    pt = screen.numinput(f"Point {i+1}", "Val:", 0, minval = INPUT_RANGE[0], maxval = INPUT_RANGE[1])
    if (pt != None):
        graph.plot_point(trl, (i+1,pt))

screen.exitonclick()


