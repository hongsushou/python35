class Settings():

    def __init__(self):
        #屏幕设置
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (100, 200, 168)
        self.ship_speed_factor = 0.8


        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (232, 232, 232)
        self.bullet_speed_factor = 0.1
        self.bullets_allowed = 200

        #外星人设置
        self.alien_mind = 2 #外星人间隔设置
        
