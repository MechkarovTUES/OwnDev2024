import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Follow the Cursor')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the point
point_radius = 5

def lerp(start, end, t):
    return start + t * (end - start)

class Joint:
    def __init__(self, x, y, radius, max_distance, atr):
        self.x = x
        self.y = y
        self.angle = 0
        self.radius = radius
        self.max_distance = max_distance
        self.atr = atr
        spine.append(self)
        self.connections = [[0, 0]]

    def draw(self, i):
        pygame.draw.circle(window, white, (int(self.x), int(self.y)), self.radius, 2)
        if i < len(self.connections):
            pygame.draw.circle(window, red, (int(self.connections[i][0]), int(self.connections[i][1])), 2)

    def follow(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)

        if distance > self.max_distance:
            self.angle = math.atan2(dy, dx)
            self.x = target_x - math.cos(self.angle) * self.max_distance
            self.y = target_y - math.sin(self.angle) * self.max_distance
    def points(self, i):
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        if i < len(self.connections):
            self.connections[i] = (x, y)
        else:
            self.connections.append((x, y))
        print(self.angle)
    def fluid(self, target_x, target_y):
        self.x = lerp(self.x, target_x, self.atr)
        self.y = lerp(self.y, target_y, self.atr)

    
# Create the spine (snake) joints
spine = []
scale = 1
max_distance = 40/scale
size = np.array([68, 84, 87, 85, 83, 77, 64, 60, 51, 38, 34, 32, 19, 15])/scale

num_joints = len(size)
for i in range(num_joints):
    Joint(width // 2, height // 2, size[i], max_distance, 0.01)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    spine[0].fluid(mouse_x, mouse_y)

    # Make each joint follow the previous one, maintaining a fixed distance
    for i in range(1, len(spine)):
        spine[i].follow(spine[i - 1].x, spine[i - 1].y)
        spine[i].points(i)

    # Clear the screen
    window.fill(black)

    # Draw the joints
    for joint in spine:
        joint.draw(spine.index(joint))
    # Update the displa
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()