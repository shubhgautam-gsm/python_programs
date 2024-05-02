import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def draw_random_face():
    fig, ax = plt.subplots()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Face
    face = patches.Ellipse(xy=(0, 0), width=8, height=10, angle=0, edgecolor='black', facecolor='white')
    ax.add_patch(face)

    # Eyes
    eye_size = random.uniform(0.5, 1.5)
    eye_x = random.uniform(-2.5, 2.5)
    eye_y = random.uniform(2, 4)
    eye_center = (eye_x, eye_y)
    eye_radius = eye_size / 2
    iris_radius = eye_radius * 0.7
    pupil_radius = iris_radius * 0.3

    left_eye = patches.Circle(xy=eye_center, radius=eye_radius, edgecolor='black', facecolor='white')
    iris_left = patches.Circle(xy=eye_center, radius=iris_radius, edgecolor='black', facecolor=random.choice(['blue', 'green', 'brown']))
    pupil_left = patches.Circle(xy=eye_center, radius=pupil_radius, edgecolor='black', facecolor='black')

    right_eye = patches.Circle(xy=(eye_x * -1, eye_y), radius=eye_radius, edgecolor='black', facecolor='white')
    iris_right = patches.Circle(xy=(eye_x * -1, eye_y), radius=iris_radius, edgecolor='black', facecolor=random.choice(['blue', 'green', 'brown']))
    pupil_right = patches.Circle(xy=(eye_x * -1, eye_y), radius=pupil_radius, edgecolor='black', facecolor='black')

    ax.add_patch(left_eye)
    ax.add_patch(iris_left)
    ax.add_patch(pupil_left)
    ax.add_patch(right_eye)
    ax.add_patch(iris_right)
    ax.add_patch(pupil_right)

    # Eyebrows
    eyebrow_size = random.uniform(0.5, 1.5)
    eyebrow_x = random.uniform(-3, 3)
    eyebrow_y = random.uniform(1, 2)
    eyebrow_points = [(eyebrow_x - eyebrow_size / 2, eyebrow_y),
                      (eyebrow_x, eyebrow_y + eyebrow_size / 3),
                      (eyebrow_x + eyebrow_size / 2, eyebrow_y)]
    left_eyebrow = patches.Polygon(xy=eyebrow_points, edgecolor='black', facecolor='black')

    eyebrow_x = random.uniform(-3, 3)
    eyebrow_y = random.uniform(1, 2)
    eyebrow_points = [(eyebrow_x - eyebrow_size / 2, eyebrow_y),
                      (eyebrow_x, eyebrow_y + eyebrow_size / 3),
                      (eyebrow_x + eyebrow_size / 2, eyebrow_y)]
    right_eyebrow = patches.Polygon(xy=eyebrow_points, edgecolor='black', facecolor='black')

    ax.add_patch(left_eyebrow)
    ax.add_patch(right_eyebrow)

    # Nose
    nose_size = random.uniform(0.5, 1.5)
    nose_x = random.uniform(-1, 1)
    nose_y = random.uniform(0, 1)
    nose_points = [(nose_x, nose_y),
                   (nose_x + nose_size / 2, nose_y + nose_size),
                   (nose_x - nose_size / 2, nose_y + nose_size)]
    nose = patches.Polygon(xy=nose_points, edgecolor='black', facecolor='red')
    ax.add_patch(nose)

    # Mouth
    mouth_size = random.uniform(0.5, 1.5)
    mouth_x = random.uniform(-2, 2)
    mouth_y = random.uniform(-1, 0)
    mouth_center = (mouth_x, mouth_y)
    mouth_width = mouth_size
    mouth_height = mouth_size * 0.5
    mouth_points = [
        (mouth_center[0] - mouth_width / 2, mouth_center[1]),
        (mouth_center[0] - mouth_width / 2, mouth_center[1] - mouth_height),
        (mouth_center[0] + mouth_width / 2, mouth_center[1] - mouth_height),
        (mouth_center[0] + mouth_width / 2, mouth_center[1])
    ]
    # Adjust mouth curve based on random expression (e.g., smile, frown)
    if random.random() > 0.5:
        mouth_points[1] = (mouth_points[1][0], mouth_points[1][1] + mouth_height * 0.2)
        mouth_points[2] = (mouth_points[2][0], mouth_points[2][1] + mouth_height * 0.2)
    mouth = patches.Polygon(xy=mouth_points, edgecolor='black', facecolor='red')
    ax.add_patch(mouth)

    # Ears
    ear_size = random.uniform(0.5, 1.5)
    ear_x = random.uniform(-3.5, 3.5)
    ear_y = random.uniform(1, 3)
    ear_center = (ear_x, ear_y)
    ear_radius = ear_size / 2
    ear = patches.Ellipse(xy=ear_center, width=ear_radius, height=ear_radius * 1.5, angle=0, edgecolor='black', facecolor='white')
    ax.add_patch(ear)

    ear_x = random.uniform(-3.5, 3.5)
    ear_y = random.uniform(1, 3)
    ear_center = (ear_x, ear_y)
    ear = patches.Ellipse(xy=ear_center, width=ear_radius, height=ear_radius * 1.5, angle=0, edgecolor='black', facecolor='white')
    ax.add_patch(ear)

    # Hair
    hair_size = random.uniform(2, 5)
    hair_x = random.uniform(-5, 5)
    hair_y = random.uniform(4, 6)
    hair_points = [
        (hair_x - hair_size / 2, hair_y),
        (hair_x, hair_y + hair_size),
        (hair_x + hair_size / 2, hair_y),
        (hair_x + hair_size / 2, hair_y - hair_size * 0.3),
        (hair_x - hair_size / 2, hair_y - hair_size * 0.3)
    ]
    hair = patches.Polygon(xy=hair_points, edgecolor='black', facecolor=random.choice(['black', 'brown', 'blonde']))
    ax.add_patch(hair)

    plt.show()

draw_random_face()
