import pygame.font


class Button():
    """Class for button object"""
    
    
    def __init__(self, game_settings, screen, msg):
        """Init button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Button attributes - size, color, font
        self.width = 200
        self.height = 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        # Build the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Prepare graphical text
        self.prepare_msg(msg)
        
        
    def prepare_msg(self, msg):
        """Convert text message to graphics and center with button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
            
            
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)