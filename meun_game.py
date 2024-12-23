import pygame
import sys
pygame.init()
#กำหนดขนาดหน้าจอ
screen_width = 800
screen_height = 600
scree = pygame.display.set_mode((screen_width,screen_height))
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
            if event.key == pygame.K_RETURN:
                game_loop()
        screen.fill(WHITH)
        draw_text("Main Menu",64,BLACK,WIDTH // 2 , screen_height // 2 - 50)
        draw_text("Press Enter to Start", 36 ,BLACK , screen_width // 2 , screen_height // 2)
        pygame.display.flip()
        clock.tick(FPS)
#ฟังก์ชันหลัก

        

