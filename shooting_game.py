# กำหนดคลาสสำหรับกระสุน
class Bullet(pygame.sprite.sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((5, 10))
