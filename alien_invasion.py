from settings import Settings
from ship import Ship
import pygame
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Make the play button
    play_button = Button(ai_settings, screen, "Play")

    #Create and instance to store game statistics
    stats = GameStats(ai_settings)

    #Make a ship, a group of aliens, and a group of bullets
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Starts main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
