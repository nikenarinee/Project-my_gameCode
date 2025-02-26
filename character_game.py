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
        super().__init__()  # เรียก constructor ของ Sprite
        self.image = pygame.Surface((5, 10))  # สร้างพื้นผิว (surface) ของกระสุน
        self.image.fill(RED)  # กำหนดสีของกระสุนเป็นสีแดง
        self.rect = self.image.get_rect()  # สร้าง rect เพื่อใช้ในการจัดตำแหน่ง
        self.rect.center = (x, y)  # ตั้งตำแหน่งของกระสุนให้ตรงกับพิกัดที่ส่งมาจากภายนอก

    def update(self):
        self.rect.y -= 10  # เคลื่อนที่กระสุนขึ้นไป (ลดค่า y)
        if self.rect.bottom < 0:  # ถ้ากระสุนออกนอกหน้าจอ
            self.kill()  # ลบกระสุนออกจาก sprite group

# การทดสอบการสร้าง Bullet และเพิ่มเข้าไปใน sprite group
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    all_sprites = pygame.sprite.Group()  # สร้าง sprite group

    # สร้าง Bullet และเพิ่มเข้าไปในกลุ่ม
    bullet = Bullet(400, 500)
    all_sprites.add(bullet)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # อัปเดตทุก sprite ในกลุ่ม
        all_sprites.update()

        # วาดทุก sprite ลงบนหน้าจอ
        screen.fill((255, 255, 255))  # ตั้งพื้นหลังเป็นสีขาว
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()