from pygame import *


class Menu:
    def __init__(self):
        self.surfaces = []
        self.callbacks = []
        self.current_option_index = []

    def append_option(self, option, callback):
        self.current_option_index.append(calibri_50.render(option, True, Color('White')))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.surfaces) - 1))

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                draw.rect(surf, Color(0, 255, 0), option_rect)
            surf.blit(option, option_rect)


init()
size = (800, 600)
screen = display.set_mode(size)
display.set_caption('PuzzleGame')
calibri_50 = font.SysFont('calibri', 50)
screen.fill('BLACK')
menu = Menu()
menu.append_option('Hello world!', lambda: print('hello world!'))
menu.append_option('Quit', quit)
running = True
display.flip()
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    menu.draw(screen, 100, 100, 75)
    display.flip()


quit()


