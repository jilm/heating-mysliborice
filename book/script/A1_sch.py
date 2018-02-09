from Canvas import Square

class Scheme:

    def __init__(self, canvas):
        self.canvas = canvas
        
class ScaledScheme(Scheme):

    def __init__(self, canvas):
    

class CabinetPosition:
    
    def __init__(self, n_modules):
        self.n_modules = n_modules
        self.content = List(n_modules)
        
    def draw_face_view(self, scheme):
        

class Cabinet:

    dimensions = (360.0, 540.0)
    n_positions = 3
    n_modules = (16, 16, 16) 
    
    def __init__(self):
        self.content = (CabinetPosition(self.n_modules[n]) for n in n_modules)

    def draw_face_view(self, scheme):
        scheme.draw_rect(dimensions)
        scheme.pushmove(0, 120.0)
        for p in self.content:
            p.draw_face_view(scheme)
            scheme.move(0,150.0)        



class Quido88:

    dimensions = (137.4, 96.5, 20)

    def draw_face_view(self, scheme):
        scheme.draw_rect(dimensions)
        scheme.draw_circle(3.2, (64.45, 40.0))
        scheme.draw_circle(3.2, (-64.45, 40.0))
        scheme.draw_circle(3.2, (64.45, -40.0))
        scheme.draw_circle(3.2, (-64.45, -40.0))
            
    


# Vykres velikosti A3
# Vykresovy list
DRAWING_FRAME_SIZE = (400.0, 277.0)
GRID_FRAME_SIZE = (420.0, 297.0)
OUTER_FRAME_SIZE = (430.0, 307.0)
RAW_PAPER_SIZE = (436.0, 313.0)


draw_rect(OUTER_FRAME_SIZE) # draw outer frame
draw_rect(GRID_FRAME_SIZE)  # 
draw_rect(DRAWING_FRAME_SIZE)

# draw center marks
x, y = GRID_FRAME_SIZE
x, y = 0.5 * x, 0.5 * y
size = GRID_FRAME_SIZE[0] - DRAWING_FRAME_SIZE[0]
draw_hline(x, 0, size)
draw_hline(-x, 0, -size)
draw_vline(0, y, size)
draw_vline(0, -y, -size)

# draw grid
size = 0.5 * size
dist = 0.5 * GRID_FRAME_SIZE[0] / 3   
for i in range(2):
    draw_vline((i+1)*dist, y, size)
    draw_vline(-dist*(i+1), y, size)                
    draw_vline((i+1)*dist, -y, -size)
    draw_vline(-dist*(i+1), -y, -size)                

dist = 0.5 * GRID_FRAME_SIZE[1] / 2   
for i in range(1):
    draw_hline(x, (i+1)*dist, size)
    draw_hline(x, -dist*(i+1), size)                
    draw_hline(-x, (i+1)*dist, -size)
    draw_hline(-x, -dist*(i+1), -size)

# draw cut marks

