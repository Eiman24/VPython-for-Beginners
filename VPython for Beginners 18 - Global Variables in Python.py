from vpython import *

# electrom = sphere(pos = vector(0,0,0), radius = 0.1, color = color.green,
#                   velocity = vector(0,0,0), mass = 9.11e-33, charge = -1.6e-19,
#                   spin = 0.5)
#
# print(electrom.mass)

global speed_of_light
speed_of_light = 3e8

class particle:
    def __init__(self, position, velocity, mass, charge, spin, color):
        if velocity is None:
            self.velocity = vector(0,0,0)
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.charge = charge
        self.spin = spin
        self.body = sphere(pos = vector(0,0,0), radius = 0.1, color = color)

    def linear_momentum(self):
        return self.mass*self.velocity

    def rest_energey(self):
        global speed_of_light
        print("I am in rest_energy, and speed of light = ", speed_of_light)
        return self.mass * speed_of_light**2

electron = particle(position=vector(0, 0, 0), velocity = vector(0,0,0),
                    mass = 9.11e-33, charge = -1.6e-19, spin = 0.5, color = color.cyan)

print(electron.mass)
print(electron.linear_momentum())
print(electron.rest_energey())
print("I am in main code rest_energy, and speed of light = ", speed_of_light)