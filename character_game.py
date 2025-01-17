class Player(pagame.sprite.Sprite):
    def__init__(self):
    super().__init__()
    self.image = pygame.Surface((50,50))
    self.image.fill(BLACK)
    self.rect = self.image.get_rect()
