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
     def