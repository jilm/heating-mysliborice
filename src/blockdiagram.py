
from schema.canvas import Path
from schema.canvas import Canvas

GS = 12.0 # zakladni velikost nejakeho domneleho gridu

# Schematicky blokovy diagram topeni v podkrovi

# Krbova kamna

# Cerpadlo krbovych kamen

# Termostaticky regulacni ventil

# Smesovaci ventil
v = 0.866 * GS
path = Path()
path.move_to((0.0, 0.0))
path.line_to((v, 0.5 * GS))
path.line_to((v, -0.5 * GS))
path.line_to((-v, 0.5 * GS))
path.line_to((-v, -0.5 * GS))
path.line_to((0.0, 0.0))
path.line_to((0.5 * GS, v))
path.line_to((-0.5 * GS, v))
path.close()

# Cerpadlo do topeni

# Topeni

canvas = Canvas()
path.write(canvas)
