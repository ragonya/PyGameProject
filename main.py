from pygame import *


init()
size = (1200, 800)
screen = display.set_mode(size)
display.set_caption('PuzzleGame')
calibri_50 = font.SysFont('calibri', 50)
running = True
screen.fill('BLACK')
display.flip()


class Menu:
    def __init__(self):
        self.surfaces = []
        self.callbacks = []
        self.current_option_index = []

    def append_option(self, option, callback):
        self.current_option_index.append(calibri_50.render(option, True, Color('White')))


while running:
    for event in event.get():
        if event.type == QUIT:
            running = False


quit()


