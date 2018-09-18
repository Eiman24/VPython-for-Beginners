from vpython import *

w = 1
h = 1

ell_shape = shapes.ellipse(width = w, height = h)

ell_path = [vector(0,0,0), vector(0,0,0.1)]

ell = extrusion(path = ell_path, shape = ell_shape, opacity = 0.5)

ell.color = color.red

semimajor_axis = curve(ell.pos, ell.pos + vector(1,0,0)*w)
semiminor_axis = curve(ell.pos, ell.pos + vector(0,1,0)*h)

def eccentricity(w, h):
    major = max(w, h)
    minor = min(w, h)
    return sqrt(1-minor**2/major**2)

print(eccentricity(w, h))

ellipsoid(pos = vector(0,2,0), length = 0.1, height = 0.3, width = 1.0)