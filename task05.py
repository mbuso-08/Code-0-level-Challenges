# x,y,z represents three sides of a triangle
x = int(3)
y = int(4)
z = int(5)

# semiperimeter calculation
s = (1/2) * (x + y + z)

area = (s*(s - x) * (s - y) * (s - z)) ** (1/2)
print(area)