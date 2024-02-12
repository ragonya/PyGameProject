from pygame import *


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (self.width, self.height))

        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = image.load(hover_image_path)
            self.hover_image = transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.sound = None
        if sound_path:
            self.sound = mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        ft = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 30)
        text_surface = ft.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, e):
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            event.post(event.Event(USEREVENT, button=self))
