import pgzrun
import random
import itertools

HEIGHT=400
WIDTH=400
TITLE= "SHIP ANIMATION"

coordinatesofblock=[(40,40),(360,40),(360,360),(40,360)]
coordinates=itertools.cycle(coordinatesofblock)

def draw():
    screen.clear()
    ship.draw()
    block.draw()

ship=Actor('ship')
block=Actor('block')
ship.pos=200,200
block.pos=40,40

def blockanimation():
    animation=animate(block,"bounce_end",duration=1,pos=next(coordinates))
clock.schedule_interval(blockanimation,1)

def shipanimation():
  animation2=animate(ship,"accel_decel",duration=1.5,pos=ship.target,on_finished=shiptarget)
    
def shiptarget():
    x=random.randint(100,300)
    y=random.randint(100,300)
    ship.target=x,y
    angle=ship.angle_to(ship.target)
    animate(ship,angle=angle,duration=1,on_finished=shipanimation)
shiptarget()
pgzrun.go()