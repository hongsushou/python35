import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """在飞船所处的位置创建一颗子弹"""
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.top)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

        #发射子弹的标志
        self.space = False

    def update(self):
        self.y -= self.speed_factor
        #print(self.y)
        #x = self.y
        self.rect.y = self.y
        return self.rect.y #print(float(self.rect.y)) #use for testing

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
