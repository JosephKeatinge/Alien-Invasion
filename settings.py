import pygame

class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 750
        self.screen_height = 500
        self.bg_colour = (230, 230, 230)

        #Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #Fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #Button settings
        self.button_width, self.button_height = 200, 50
        self.button_colour = (0, 255, 0)
        self.button_text_colour = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)
