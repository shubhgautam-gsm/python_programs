import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_random_face():
    # Generate random parameters for the face
    num_points = 1000
    x = np.random.normal(size=num_points)
    y = np.random.normal(size=num_points)
    z = np.random.normal(size=num_points)

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(x, y, z, c='b', marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Random 3D Face Sketch')

    # Show plot
    plt.show()

# Generate a new random face sketch
generate_random_face()
