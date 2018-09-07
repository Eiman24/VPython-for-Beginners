
G = 6.67e-11 # Gravitation constant
m1 = 2e30 # Mass of sun
m2 = 6e24 # Mass of earth
r = 150e9 # Distance between sun and earth

Force = G*m1*m2/r**2

print("Force = ", Force, " newtons" )

roundedforce = '{:0.2e}'.format(Force)
print(roundedforce)

print(round(1.3), round(1.55))