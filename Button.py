import Globals as g

class Button():
    #This class assumed a rect button
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.color = color
        self.button = g.pygame.Rect(x, y, width, height)

    #Check if the mouse position is within the correct boundary
    #returns true if the mouse position is inside of the button
    def mouse_is_in_boundary(self, position):
        x = position[0]
        y = position[1]
        if x >= self.x and y >= self.y:
            if x < self.width and y < self.height:
                return True
        return False
    
    #Changes color AND redraws button
    def change_color(self, color):
        self.color = color
    
    #REQUIRES: pygame screen as scr
    def draw(self, scr):
        g.pygame.draw.rect(scr, self.color, self.button)