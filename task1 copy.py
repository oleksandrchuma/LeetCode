import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#R(1)=  0.0000000  5.0900000  5.0900000  G(1)= -0.0982318  0.0982318  0.0982318
# R(2)=  5.0900000  0.0000000  5.0900000  G(2)=  0.0982318 -0.0982318  0.0982318
# R(3)=  5.0900000  5.0900000  0.0000000  G(3)=  0.0982318  0.0982318 -0.0982318
lattice_vectors = np.array([
    [-10, 10, 10],
    [10, -10, 10],
    [10, 10, -10]
])   # scale by acell

# Define atomic positions in reduced coordinates
atomic_positions = np.array([
    [0.0, 0.0, 0.0],  # First atom (Si)
    [0.25, 0.25, 0.25]  # Second atom (Si)
])  # scale by acell

# Generate the full crystal lattice by repeating the primitive cell
n_cells = 2  # Number of cells to repeat in each direction
atoms = []

for i in range(n_cells):
    for j in range(n_cells):
        for k in range(n_cells):
            # Translate the atomic positions by the lattice vectors
            translation = i * lattice_vectors[0] + j * lattice_vectors[1] + k * lattice_vectors[2]
            for atom in atomic_positions:
                atoms.append(atom + translation)

atoms = np.array(atoms)

# Plot the crystal structure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')

# Plot silicon atoms
#ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], c='b', label='Si atoms')

# Plot lattice vectors
origin = np.zeros(3)
for vec in lattice_vectors:
    ax.quiver(*origin, *vec, color='r', normalize=False)

# Label axes
ax.set_xlabel('X (Bohr)')
ax.set_ylabel('Y (Bohr)')
ax.set_zlabel('Z (Bohr)')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
#ax.set_title('Crystal Structure of Si with Diamond-like Lattice (2x2x2)')

# Set aspect ratio to be equal
#ax.set_box_aspect([10, 10, 10])
plt.show()