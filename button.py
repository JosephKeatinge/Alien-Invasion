import pygame

class Button():

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Get the dimensions and properties of the button
        self.width, self.height = ai_settings.button_width, ai_settings.button_height
        self.colour = ai_settings.button_colour
        self.text_colour = ai_settings.button_text_colour
        self.font = ai_settings.button_font

        #Build the button's rect object and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into rendered image and centre text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw a blank button and then draw message
        self.screen.fill(self.colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)