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

