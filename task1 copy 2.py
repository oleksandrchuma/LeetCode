import numpy as np

def calculate_reciprocal_lattice(a1, a2, a3):
    # Convert input vectors to numpy arrays
    a1 = np.array(a1)*10.18
    a2 = np.array(a2)*10.18
    a3 = np.array(a3)*10.18

    # Calculate the volume of the parallelepiped formed by a1, a2, a3
    volume = np.dot(a1, np.cross(a2, a3))

    # Calculate reciprocal lattice vectors
    b1 =  np.cross(a2, a3) / volume
    b2 =  np.cross(a3, a1) / volume
    b3 =  np.cross(a1, a2) / volume

    return b1, b2, b3

# Example input Cartesian vectors
a1 = [0, 0.5, 0.5]
a2 = [0.5, 0.0, 0.5]
a3 = [0.5, 0.5, 0.0]

# Calculate reciprocal lattice vectors
b1, b2, b3 = calculate_reciprocal_lattice(a1, a2, a3)

# Output the reciprocal lattice vectors
print("Reciprocal lattice vector b1:", b1)
print("Reciprocal lattice vector b2:", b2)
print("Reciprocal lattice vector b3:", b3)