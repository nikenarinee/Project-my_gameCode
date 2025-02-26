import pygame
import sys

# กำหนดค่าคงที่
WIDTH, HEIGHT = 800, 600
FPS = 60

# เริ่มต้น Pygame
pygame.init()
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

        screen.fill(WHITH)
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

        

