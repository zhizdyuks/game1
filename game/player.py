

class Ship(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h    
        self.pos = PVector(self.w, self.h)
        self.r = 20
        self.heads = (0)
        self.vel = PVector(0,0)
        self.rotation = 0.0
        self.isBoosting = False
        
        
        
    
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.heads + PI / 2)
        triangle(-self.r, self.r, self.r, self.r, 0, -self.r)
        popMatrix()
        
    def setRotation(self, angle):
        self.rotation = angle
        
    def thrusting(self, arg):
        self.isBoosting = arg
                        
    def turn(self):
        self.heads += self.rotation
        
    def thrust(self):
        force = PVector.fromAngle(self.heads)
        force.mult(0.1)
        self.vel.add(force)
        #print(self.vel)
        
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
        if (self.isBoosting):
            self.thrust()
        self.pos.add(self.vel)
        self.vel.mult(0.99)
        
        
