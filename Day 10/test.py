# Importing the gcd function from the math module
from math import gcd

# Number of vertices in the polygon
n = 4

# Arrays to store the x and y coordinates of the vertices
# Each lattice point will be represented by (x[i], y[i])
x = [0, 4, 4, 0]
y = [0, 0, 4, 4]

# Close the polygon by setting the last vertex equal to the first
x.append(x[0])
y.append(y[0])

# Variable to store the area of the polygon
area = 0

# Calculate the area of the polygon using the shoelace formula
for i in range(n):
    area += x[i] * y[i + 1]
    area -= y[i] * x[i + 1]
area = abs(area)

# Variable to store the number of boundary points
boundary = 0

# Calculate the number of boundary points
for i in range(n):
    if x[i + 1] == x[i]:
        boundary += abs(y[i + 1] - y[i])  # Vertical edge
    elif y[i + 1] == y[i]:
        boundary += abs(x[i + 1] - x[i])  # Horizontal edge
    else:
        boundary += gcd(abs(x[i + 1] - x[i]), abs(y[i + 1] - y[i]))  # Diagonal edge

# Calculate the number of interior points using Pick's theorem
interior = (area + 2 - boundary) // 2

# Print the number of interior and boundary points
print(interior, boundary)
