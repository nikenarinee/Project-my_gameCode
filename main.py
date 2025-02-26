import pygame
import sys

# กำหนดค่าคงที่
WIDTH, HEIGHT = 800, 600
FPS = 60

# เริ่มต้น Pygame
pygame.init()
#กำหนดขนาดหน้าจอ
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 600
FPS = 60
scree = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

#color
WHITH = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,225,0)
RED = (255,0,0)
#ฟังก์ชันแสดงเมนูหลัก
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        screen.fill(WHITH)
        draw_text("Main Menu",64,BLACK,WIDTH // 2,HEIGHT // 2 - 50)
        draw_text("Press Enter to Start", 36 ,BLACK , WIDTH // 2 , HEIGHT // 2)
        pygame.display.flip()
        clock.tick(FPS)
        scree.fill(WHITH)
        draw_text('Main Menu', 64 , BLACK,WIDTH// 2,HEIGHT // 2 - 50)
        draw_text('Press Enter to Start', 36 , BLACK,WIDTH // 2,HEIGHT // 2 )
        draw_text("Main Menu", 64, BLACK, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Press Enter to Start", 36, BLACK, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        clock.tick(FPS)
#ฟังก์ชันสำหรับเกม
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WIDTH)
        draw_text('Game Running...',48,BLACK,WIDTH//2 , HEIGHT // 2 )
        draw_text("Game Running...", 48, BLACK, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        clock.tick(FPS)

#ฟังก์ชันการวาดข้อความ
def draw_text(text, size, color, x, y) :
    font = pygame. font. Font (None, size)
    text_surface = font. render (text, True, color)
    text_rect = text_surface.get_rect (center=(x, y))
    screen. blit (text_surface, text_rect)
# ฟังก์ชั่นหลัก
def main() :
    global screen, clock
    pygame. init ( )
    screen = pygame.display.set_mode ( (WIDTH, HEIGHT))
    pygame.display.set_caption ("Game with Menu")
    clock = pygame. time.Clock ()

    main_menu ()
if __name__ == "__main__":
    main ()
import pygame
import random
import math

RED = (255, 0, 0)
WIDTH = 800  
HEIGHT = 600  
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
    def updete(self):
        #คำนวนทิศทางไปยังผู้เล่น
        direction_x = self.player.rect.centerx-self.rect.centerx
        direction_y = self.player.rect.centerx-self.rect.centerx
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
import pygame
# Define the color RED
RED = (255, 0, 0)
# กำหนดคลาสสำหรับกระสุน
class Bullet(pygame.sprite.sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
             self.kill()
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