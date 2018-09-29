class Asteroid(object):
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.r = int(random(15, 50))
        self.edges_num = int(random(5, 15))
        
        
    def render(self):
        pushMatrix()
        stroke(255)

        translate(self.pos.x, self.pos.y)
        # ellipse(0, 0, self.r, self.r)
        beginShape()
        for i in range(self.edges_num):
            angle = map(i, 0, self.edges_num, 0, TWO_PI)
            x = self.r * cos(angle)
            y = self.r * sin(angle)
            vertex(x, y)
        endShape(CLOSE)
        
        
        popMatrix()
