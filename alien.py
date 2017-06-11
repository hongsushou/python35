import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    创建一个外星人的类
    """
    def __init__(self, settings, screen):
        """
        初始化外星人函数
        """
        super(Alien, self).__init__()
        self.settings = settings
        self.screen = screen

        self.image = pygame.image.load(r"images/alien2.png")
        self.rect = self.image.get_rect()
        #self.screen_rect = self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
