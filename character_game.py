import pygame
import random
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 600

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # ขนาดกระสุน
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def update(self):
        self.rect.y -= 10  # กระสุนจะเคลื่อนที่ขึ้น
        if self.rect.bottom < 0:  # ถ้ากระสุนออกจากจอ
            self.kill()  # ลบกระสุนออกจากเกม


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # ขนาดของผู้เล่น
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # ตั้งตำแหน่งเริ่มต้นที่กลางจอ
        self.score = 0

def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)