import math
grav_con = 6.6743 * (10**-11)
mass = float(input("Input mass in kg:"))
radius = float(input("Input radius in metres:"))
escape_vel = math.sqrt((2*grav_con*mass)/radius)

print("escape velocity required in m/s is:", escape_vel)
