from pygame import *
from scripts import button


init()
size = (1200, 800)
screen = display.set_mode(size)
display.set_caption('PuzzleGame')

icon = image.load('images/icon/icon.png')
bg_main = image.load('images/backGround/bg_main.png')
bg_settings = image.load('images/backGround/bg_settings.png')
bg_help = image.load('images/backGround/bg_help.png')
display.set_icon(icon)

PuzzleGame_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
PuzzleGame_surface = PuzzleGame_txt.render('PuzzleGame', True, (230, 143, 85))
main_font = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 15)

display.flip()
play_button = button.Button(1200/2-(252/2), 200, 252, 74, "Play", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')


def main_menu():
    running = True
    while running:
        screen.blit(bg_main, (0, 0))
        screen.blit(PuzzleGame_surface, (350, 50))
        play_button.draw(screen)
        for e in event.get():
            if e.type == QUIT:
                running = False
            play_button.handle_event(e)

        play_button.check_hover(mouse.get_pos())
        display.flip()


main_menu()
quit()
