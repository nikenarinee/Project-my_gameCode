import pygame
from src.player import Player
from src.enemy import Enemy

class ShootingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(375, 500)
        self.enemies = [Enemy(100, 50), Enemy(300, 100), Enemy(500, 50)]

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))  # พื้นหลังสีดำ
            keys = pygame.key.get_pressed()
            self.player.move(keys)

            for enemy in self.enemies:
                enemy.move()
                enemy.draw(self.screen)

            for bullet in self.player.bullets:
                bullet.move()
                bullet.draw(self.screen)

            self.player.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()