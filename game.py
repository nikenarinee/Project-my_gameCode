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
#กำหนดตำแหน่งตัวละคร
player_x = screen_width // 2
player_y = screen_height // 2
player_width = 50
player_height = 50
player_speed = 5
#loop
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
    #keys
    keys = pygame.key.get_pressed()
