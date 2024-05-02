from PIL import Image, ImageDraw, ImageFilter
import random

def generate_random_face(width=400, height=600):
    # Create a new blank image
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Draw a random face
    draw_face(draw, width, height)

    # Show the generated face
    img.show()

def draw_face(draw, width, height):
    # Draw a random face shape
    face_shape = random.choice(['circle', 'oval', 'square'])
    if face_shape == 'circle':
        draw.ellipse([(50, 50), (width - 50, height - 50)], fill=random_skin_color())
    elif face_shape == 'oval':
        draw.ellipse([(50, 50), (width - 50, height - 100)], fill=random_skin_color())
    else:
        draw.rectangle([(50, 50), (width - 50, height - 50)], fill=random_skin_color())

    # Draw eyes
    eye_color = random.choice(['blue', 'green', 'brown'])
    draw_eyes(draw, width, height, eye_color)

    # Draw nose
    draw_nose(draw, width, height)

    # Draw mouth
    draw_mouth(draw, width, height)

def draw_eyes(draw, width, height, color):
    eye_size = 30
    eye_distance = 70
    eye_y = height // 3

    draw.ellipse([(width // 2 - eye_distance, eye_y), (width // 2 - eye_distance + eye_size, eye_y + eye_size)], fill=color)
    draw.ellipse([(width // 2 + eye_distance - eye_size, eye_y), (width // 2 + eye_distance, eye_y + eye_size)], fill=color)

def draw_nose(draw, width, height):
    nose_size = 20
    nose_y = height // 2 - 20

    draw.polygon([(width // 2 - nose_size, nose_y), (width // 2, nose_y + nose_size), (width // 2 + nose_size, nose_y)], fill='saddlebrown')

def draw_mouth(draw, width, height):
    mouth_y = height // 2 + 50
    mouth_width = 60
    mouth_height = 20

    draw.rectangle([(width // 2 - mouth_width // 2, mouth_y),
                    (width // 2 + mouth_width // 2, mouth_y + mouth_height)], fill='pink')

def random_skin_color():
    # You can add more skin tones as needed
    skin_tones = ['#FFDAB9', '#F0D5BE', '#E0C9B5', '#C9AD95']
    return random.choice(skin_tones)

# Generate a new random face
generate_random_face()
