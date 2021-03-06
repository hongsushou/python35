import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    初始化游戏并创建一个屏幕对象
    """
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #一个用于存储子弹的编组
    bullets = Group()
    ship = Ship(settings, screen)
    aliens = Group()

    #创建外星人群
    gf.create_fleet(settings, screen, aliens)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets) #更新子弹位置并删除消失的子弹
        #print(len(bullets))
        #绘制新屏幕内容
        gf.update_screen(settings, screen, ship, bullets, aliens)

if __name__ == "__main__":
    run_game()
