import sys

import pygame
from bullet import Bullet
from alien import Alien


def fire_bullet(settings, bullets, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keys_down(event, ship, settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, bullets, screen, ship)

def check_keys_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    #elif event.key == pygame.K_SPACE:
    #    bullet.space = False

def check_events(settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keys_down(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keys_up(event, ship)

def update_screen(settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(settings.bg_color) #每次循环都会绘制背景
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #让最近绘制的屏幕可见
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update() #更新子弹的位置
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(alien_width, settings):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(settings, screen, aliens, alien_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.x / settings.alien_mind
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    #创建第一行外星人
    number_aliens_x = get_number_aliens_x(alien.rect.width, settings)  #调用函数得到一行屏幕容纳外星人数
    for alien_number in range(number_aliens_x):
        create_alien(settings, screen, aliens, alien_number)   #调用创建外星人函数
