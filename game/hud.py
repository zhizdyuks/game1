class Hud(object):
    """Aim calculating and drawing class."""
    def __init__(self):
        self.x = 0
        self.y = 0

    def aim_draw(self):
        self.x, self.y = mouseX, mouseY
        ellipse(self.x, self.y, 10, 10)
