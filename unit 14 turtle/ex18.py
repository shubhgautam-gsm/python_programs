import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Face Generator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a random face
def draw_face(surface, x, y):
    # Draw face
    pygame.draw.circle(surface, WHITE, (x, y), 100)

    # Draw eyes
    eye_radius = 10
    pygame.draw.circle(surface, BLACK, (x - 40, y - 30), eye_radius)
    pygame.draw.circle(surface, BLACK, (x + 40, y - 30), eye_radius)

    # Draw nose
    pygame.draw.circle(surface, BLACK, (x, y), 5)

    # Draw mouth
    pygame.draw.arc(surface, BLACK, (x - 30, y + 20, 60, 30), 0, 3.14)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(WHITE)

    # Generate random coordinates for the face
    face_x = random.randint(50, width - 50)
    face_y = random.randint(50, height - 50)

    # Draw a random face
    draw_face(window, face_x, face_y)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
