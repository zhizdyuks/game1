import math
from player import Ship
from asteroids import Asteroid
ship = None
asteroids = []


#position of the Player spawn
sqr = 320

def setup():
    global ship, asteroids
    size(640, 640)
    ship = Ship(sqr, sqr)
    for i in range(floor(random(10, 15))):
        asteroids.append(Asteroid())


def draw():
    global ship, asteroids
    background(0)
    ship.turn()
    ship.edges()
    ship.render()
    ship.update()



    for asteroid in asteroids:
        asteroid.render()
        print("rendered")
        print(asteroid.pos.x, asteroid.pos.y, asteroid.r)





def keyReleased():
    if (keyCode == RIGHT):
        ship.isBoostingRight = False
    elif (keyCode == LEFT):
        ship.isBoostingLeft = False
    elif (keyCode == UP):
        ship.thrusting = False

def keyPressed():
    if (keyCode  == RIGHT):
        ship.isBoostingRight = True
    elif (keyCode  == LEFT):
        ship.isBoostingLeft = True
    elif (keyCode == UP):
        ship.isBoostingUp = True
