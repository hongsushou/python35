import pygame

class Ship():

    def __init__(self, settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        self.settings = settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r"images/ship.png")
        self.rect = self.image.get_rect() #获得图片的矩形
        self.screen_rect = self.screen.get_rect() #获得屏幕的矩形

        #将每艘飞船放在屏幕底部中央·确定图片摆放的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #self.rect.centery = self.screen_rect.centery

        #在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        #根据移动标注调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
