import pygame
import random
import math
# กำหนดขนาดหน้าจอ
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#คลาสสำหรับศัตรู
class Enemy(pygame.sprite.Sprite):
    def _init_ (self, player):
         super().__init__()
         self.image = pygame. Surface((50, 50))
         self.image.fill(RED)
         self.rect = self.image.get_rect()
         self.rect.x = random.randint (0, WIDTH)
         self.rect.y = random.randint(0, HEIGHT)
         self.player = player
    def update(self):
        #คำนวนทิศทางไปยังผู้เล่น
        direction_x = self.player.rect.centerx -self.rect.centerx
        direction_y = self.player.rect.centery -self.rect.centery
        distance = math.hypot(direction_x,direction_y)

        if distance > 0:
            direction_x /= distance
            direction_y /= distance
            self.rect.x += direction_x * 2 #ความเร็วการเคลื่อนที่
            self.rect.y += direction_y * 2
