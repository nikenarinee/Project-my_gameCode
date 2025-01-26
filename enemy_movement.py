#คลาสสำหรับศัตรู
class Enemy(pygame.sprite.Sprite):
    def init (self, player):
         super().__init__()
         self.image = pygame. Surface((50, 50))
         self.image.fill(RED)
         self.rect = self.image.get_rect()
         self.rect.x random.randint (0, WIDTH)
         self.rect.y = random.randint(0, HEIGHT)
         self.player = player
     def updete(self):
        #คำนวนทิศทางไปยังผู้เล่น
        direction_x = self.player.rect.centerx.-self.rect.centerx
        direction_y = self.player.rect.centerx.-self.rect.centerx
        distance = math.hypot(direction_x,direction_y)

        if distance > 0:
            direction_x /= distance
            direction_y /= distance
            self.rect.x += direction_x * 2 #ความเร็วการเคลื่อนที่
            self.rect.y += direction_y * 2
