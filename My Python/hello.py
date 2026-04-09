# print("Hello World")
from vpython import *

balls=[sphere(radius=0.2,pos=vector(i,0,0)) for i in range(10)]

while True:
    rate(30)
    for b in balls:
        b.pos.x+=0.05
# from vpython import *

# c1=box(pos=vector(-2,0,0))
# c2=box(pos=vector(2,0,0),color=color.blue)

# while True:
#     rate(60)
#     c1.rotate(angle=0.05,axis=vector(0,1,0))
#     c2.rotate(angle=0.05,axis=vector(1,0,0))