# by Kami Bigdely
# Extract superclass.
class Shape:
    def __init__(self, visible = True):
        self.visible = visible

    def hide(self):
        self.visible = False
        
    def unhide(self):
        self.visible = True

    def display(self):
        if self.visible:
            print('Drew the shape.')


class Circle(Shape):
    
    def __init__(self, visible, x, y, r):
        super().__init__(visible)
        self.center_x = x
        self.center_y = y
        self.r = r
        
    def get_center(self):
        return self.center_x, self.center_y
    
    
class Rectangle(Shape):
    
    def __init__(self, visible, x, y, width, height):
        # left-bottom corner.
        super().__init__(visible)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(False,0,0,10)
    circle.unhide()
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(True, 10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.unhide()
    rect.display()
    print('center point',rect.get_center())