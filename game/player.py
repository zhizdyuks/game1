import math

class Ship(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.pos = PVector(self.w, self.h)
        self.r = 20
        self.heads = (0)
        self.vel = PVector(0,0)
        self.rotation = 0.0
        self.isBoostingUp = False
        self.isBoostingLeft = False
        self.isBoostingRight = False
        self.isBoostingDown = False






    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.heads)
        triangle(-self.r, self.r, self.r, self.r, 0, -self.r)
        popMatrix()



    def setRotation(self):
        """setting rotation of the object to follow the mouse """
        run, rise =  (mouseX - self.pos.x, mouseY - self.pos.y)
        self.rotation = radians(math.degrees(math.atan2(rise, run))) + PI/2


    def thrusting_up(self, arg):
        self.isBoostingUp = arg


    def turn(self):
        #self.heads += self.rotation
        self.heads = self.rotation






    def thrust_forward(self):
        force = PVector.fromAngle(3 * PI / 2)
        force.mult(0.3)
        self.vel.add(force)
        #print(self.vel)

    def thrust_right(self):
        force = PVector.fromAngle(0)
        force.mult(0.3)
        self.vel.add(force)

    def thrust_left(self):
        force = PVector.fromAngle(PI)
        force.mult(0.3)
        self.vel.add(force)

    def thrust_down(self):
        force = PVector.fromAngle(PI / 2)
        force.mult(0.3)
        self.vel.add(force)

     #detecting if ship crossed the screen edges and set
     #it coordinate to the opposite edge
    def edges(self):
        if (self.pos.x > width + self.r):
            self.pos.x = -self.r
        elif (self.pos.x < -self.r):
            self.pos.x = width + self.r
        elif(self.pos.y > height + self.r):
            self.pos.y = -self.r
        elif(self.pos.y < -self.r):
            self.pos.y = (height + self.r)

    

    def update(self):
        self.setRotation()

        if (self.isBoostingUp):
            self.thrust_forward()
            print ("Up")
        elif (self.isBoostingLeft):
            self.thrust_left()
        elif (self.isBoostingRight):
            self.thrust_right()
        elif (self.isBoostingDown):
            self.thrust_down()

        self.pos.add(self.vel)
        self.vel.mult(0.90)
