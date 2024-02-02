from pygame import *
from scripts import button
import sys


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

settings_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
settings_surface = PuzzleGame_txt.render('Settings', True, (230, 143, 85))

help_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
help_surface = PuzzleGame_txt.render('Help', True, (230, 143, 85))

display.flip()
play_button = button.Button(1200/2-(252/2), 200, 252, 74, "Play", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
difficulty_button = button.Button(1200/2-(252/2), 290, 252, 74, "Difficulty", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
settings_button = button.Button(1200/2-(252/2), 380, 252, 74, "Settings", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
help_button = button.Button(1200/2-(252/2), 470, 252, 74, "Help", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
exit_button = button.Button(1200/2-(252/2), 560, 252, 74, "Exit", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')


def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_main, (0, 0))
        screen.blit(PuzzleGame_surface, (350, 50))
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == USEREVENT and e.button == settings_button:
                settings_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == exit_button:
                sys.exit()

            if e.type == USEREVENT and e.button == play_button:
                new_game()
                sys.exit()

            if e.type == USEREVENT and e.button == help_button:
                help()
                sys.exit()

            for btn in [play_button, difficulty_button, settings_button, help_button, exit_button]:
                btn.handle_event(e)

        for btn in [play_button, difficulty_button, settings_button, help_button, exit_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()

def settings_menu():
    audio_button = button.Button(1200/2-(252/2), 200, 252, 74, "Audio", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    video_button = button.Button(1200/2-(252/2), 290, 252, 74, "Video", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    back_button = button.Button(1200/2-(252/2), 380, 252, 74, "Back", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_settings, (0, 0))
        screen.blit(settings_surface, (420, 50))
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == USEREVENT and e.button == back_button:
                main_menu()
                sys.exit()

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(e)

        for btn in [audio_button, video_button, back_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()


def help():
    back_button1 = button.Button(1200 / 2 - (252 / 2), 700, 252, 74, "Back", 'images/buttons/static_button.png', 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_help, (0, 0))
        screen.blit(help_surface, (500, 50))
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == USEREVENT and e.button == back_button1:
                main_menu()
                sys.exit()
            for btn in [back_button1]:
                btn.handle_event(e)

        back_button1.draw(screen)
        back_button1.check_hover(mouse.get_pos())
        display.flip()


def new_game():
    pass

if __name__ == '__main__':
    main_menu()
quit()
