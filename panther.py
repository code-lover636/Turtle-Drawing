import turtle

screen = turtle.getscreen()
screen.bgcolor("black")
turtle.screensize(400,400)
screen.setworldcoordinates(100,500,600,100)

tur = turtle.Turtle()
tur.shape("circle")
tur.shapesize(0.2,0.5,)
tur.color("white")
tur.pensize(3)

def jaw():
    tur.penup()
    tur.goto(331, 337)
    tur.pendown()
    tur.goto(332, 318)
    tur.goto(321, 298)
    tur.goto(311, 286)
    
    tur.penup()
    tur.goto(369,338)
    tur.pendown()
    tur.goto(369, 316)
    tur.goto(378, 298)
    tur.goto(388, 284)
    
def eyebrow():
    tur.penup()
    tur.goto(343, 273)
    tur.pendown()
    tur.goto(344, 268)
    tur.goto(324, 251)
    tur.goto(316, 260)
    
    tur.penup()
    tur.goto(357, 273)
    tur.pendown()
    tur.goto(354, 268)
    tur.goto(376, 251)
    tur.goto(383, 260)
    
def ear():
    tur.penup()
    tur.goto(315, 237)
    tur.pendown()
    tur.goto(310, 221)
    tur.goto(309, 242)  
    
    tur.penup()
    tur.goto(386, 237)
    tur.pendown()
    tur.goto(390, 223)
    tur.goto(390, 221)
    tur.goto(390, 242) 
    
def eye():
    tur.penup()
    tur.goto(329, 271)
    tur.pendown()
    tur.goto(319, 271)
    tur.goto(337, 283)
    
    tur.penup()
    tur.goto(369, 271)
    tur.pendown()
    tur.goto(380, 272)
    tur.goto(363, 283)
    tur.goto(362, 288)
    tur.goto(345, 290)
    tur.goto(337, 283)
  
    
def nano():
    tur.penup()
    tur.shape("triangle")
    tur.shapesize(0.3,3)
    tur.left(160)
    tur.goto(284, 352); tur.penup(); tur.stamp()
    cor =  [(293, 359),(303, 368),(315, 373),(330, 379),(351, 385),(369, 380),(387, 375),(400, 369),(408, 359),(417, 351)]
    for n in range(len(cor)):
        tur.goto(*cor[n]); tur.right(n+10); tur.stamp()
    tur.hideturtle()

    
jaw(); eyebrow(); ear(); eye(); nano()
tur.color("#8a1899")
tur.right(13)
jaw(); eyebrow(); ear(); eye(); nano()

def position(event):
    a, b = event.x, event.y
    print('{}, {}'.format(a, b))

ws = turtle.getcanvas()
ws.bind('<Button-1>', position)

turtle.done()