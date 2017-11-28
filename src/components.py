import functools

class Canvas:
    def __init__(self):
        self.scale = 1.0
        self.x_offset = 0.0
        self.y_offset = 0.0
        self.frame = None
    def line(self, coordinates):
        # transform given coordinates
        transform = list(((x*self.scale+self.x_offset, y*self.scale+self.y_offset) for x, y in coordinates))
        self.union(transform)
        # format into string
        form = ('({},{})'.format(x, y) for x, y in transform)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {}'.format(concat))
    def rect(self, x, y, width, height):
        self.line(((x, y), (x+width, y), (x+width, y+height), (x, y)))
    def set_scale(self, scale):
        self.scale = scale
    def scale(self, scale):
        self.scale *= scale
    def move(self, offset):
        self.x_offset += offset[0]
        self.y_offset += offset[1]
    def union(self, coordinates):
        self.frame = ((
            min((x for x, y in coordinates)),
            min((y for x, y in coordinates)), (
            max((x for x, y in coordinates)),
            max((y for x, y in coordinates))
        )))
        print(self.frame)

canvas = Canvas()
canvas.set_scale(0.5)

class Component:
    pass

class Resistor:
    def __init__(self):
        pass
    def draw_block_symbol(self):
        canvas.rect(-2.0, -6.0, 4.0, 12.0)
        canvas.line(((0.0, 6.0), (0.0, 9.0)))
        canvas.line(((0.0, -6.0), (0.0, -9.0)))
    
class PT100:
    def __init__(self):
        pass
    def draw_block_symbol(self):
        Resistor.draw_block_symbol(self)
        canvas.line(((-10.0, -5.0), (-5.0, -5.0), (5.0, 5.0)))            
    
class P5310(Component):
    def __init__(self):
        pass
    def draw_block_symbol(self):
        canvas.rect(-6.0, -6.0, 12.0, 12.0)
        canvas.line(((-6.0, -6.0), (12.0, 12.0)))
        
Resistor().draw_block_symbol()
