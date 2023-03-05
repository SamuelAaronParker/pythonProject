import math

vel = 44  # meter per second
theta = 80  # degrees
x = 0.5  # meters
def h_proj(vel, theta, x):
    g = 9.81  # acceleration due to gravity
    h = (x * math.tan(math.radians(theta))) - ((g * x**2) / (2 * vel ** 2 * math.cos(math.radians(theta)) ** 2)) + 1
    return h
h = h_proj(vel, theta, x)
# print("The height of the projectile is {:.2f} meters".format(h))
print(f"The height of the projectile is {h:.3f} meters")