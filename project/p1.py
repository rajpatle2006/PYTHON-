from vpython import *

balls=[sphere(radius=0.2,pos=vector(i,0,0)) for i in range(10)]

while True:
    rate(30)
    for b in balls:
        b.pos.x+=0.05