import pygame
import Bullet
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self) : 
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.cemter = (WIDTH // 2, HEIGHT // 2)
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.x -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
