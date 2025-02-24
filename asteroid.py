import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           (int(self.position.x), int(self.position.y)), self.radius, 2)
        # print(f"asteroid draw")

    def update(self, dt):
        # print(f"update asteroid {self.position}")
        self.position += self.velocity * dt
