from pygame import *
from scripts import button
import sys
import rick_roll
import PIL


difficulty = {1: 'easy (4 * 4)', 2: 'normal (5 * 5)', 3: 'hard (8 * 8)', 4: 'very hard (16 * 16)'}
count = 1

init()
W, H = 1280, 800
screen = display.set_mode((W, H))
display.set_caption('PuzzleGame')

icon = image.load('images/icon/icon.png')
display.set_icon(icon)

bg_main = image.load('images/backGround/bg_main.png')
bg_settings = image.load('images/backGround/bg_settings.png')
bg_help = image.load('images/backGround/bg_help.png')
bg_play = image.load('images/backGround/bg_play2.png')
bg_play_rect = image.load('images/backGround/bg_play_Rect.png')

bg_main2 = image.load('images/backGround/bg_main2.png')
bg_settings2 = image.load('images/backGround/bg_settings2.png')
bg_help2 = image.load('images/backGround/bg_help2.png')
bg_play2 = image.load('images/backGround/bg_play3.png')
bg_play_rect2 = image.load('images/backGround/bg_play_Rect2.png')

bg_main3 = image.load('images/backGround/bg_main3.png')
bg_settings3 = image.load('images/backGround/bg_settings3.png')
bg_help3 = image.load('images/backGround/bg_help3.png')
bg_play3 = image.load('images/backGround/bg_play4.png')
bg_play_rect3 = image.load('images/backGround/bg_play_Rect3.png')

PuzzleGame_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
PuzzleGame_surface = PuzzleGame_txt.render('PuzzleGame', True, (230, 143, 85))
main_font = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 15)

settings_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
settings_surface = PuzzleGame_txt.render('Settings', True, (230, 143, 85))

video_settings_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
video_settings_surface = PuzzleGame_txt.render('Video Settings', True, (230, 143, 85))

help_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
help_surface = PuzzleGame_txt.render('Help', True, (230, 143, 85))


def diff(df_bt):
    global count
    global difficulty
    del df_bt
    count += 1
    if count <= 4:
        difficulty_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, f"{difficulty[count]}",
                                          'images/buttons/static_button.png', 'images/buttons/hovered_button.png',
                                          'sound_effects/button_clicked.mp3')
        return difficulty_button
    elif count > 4:
        count = 1
        difficulty_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, f"{difficulty[count]}",
                                          'images/buttons/static_button.png', 'images/buttons/hovered_button.png',
                                          'sound_effects/button_clicked.mp3')
        return difficulty_button
    display.update()


display.flip()


def main_menu():
    global W
    play_button = button.Button(W / 2 - (252 / 2), 200, 252, 74, "Play",
                                'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png',
                                'sound_effects/button_clicked.mp3')

    difficulty_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, f"{difficulty[count]}",
                                      'images/buttons/static_button.png',
                                      'images/buttons/hovered_button.png',
                                      'sound_effects/button_clicked.mp3')

    settings_button = button.Button(W / 2 - (252 / 2), 380, 252, 74, "Settings",
                                    'images/buttons/static_button.png',
                                    'images/buttons/hovered_button.png',
                                    'sound_effects/button_clicked.mp3')

    help_button = button.Button(W / 2 - (252 / 2), 470, 252, 74, "Help",
                                'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png',
                                'sound_effects/button_clicked.mp3')

    exit_button = button.Button(W / 2 - (252 / 2), 560, 252, 74, "Exit",
                                'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png',
                                'sound_effects/button_clicked.mp3')
    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_main, (0, 0))
        elif W == 1600:
            screen.blit(bg_main2, (0, 0))
        else:
            screen.blit(bg_main3, (0, 0))
        screen.blit(PuzzleGame_surface, (W // 2 - PuzzleGame_surface.get_width() // 2, 20))

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

            if e.type == USEREVENT and e.button == difficulty_button:
                difficulty_button = diff(difficulty_button)

            for btn in [play_button, difficulty_button, settings_button, help_button, exit_button]:
                btn.handle_event(e)

        for btn in [play_button, difficulty_button, settings_button, help_button, exit_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()

def settings_menu():
    global W
    audio_button = button.Button(W / 2 - (252 / 2), 200, 252, 74, "Audio", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    video_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, "Video", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    back_button = button.Button(W / 2 - (252 / 2), 380, 252, 74, "Back", 'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_settings, (0, 0))
        elif W == 1600:
            screen.blit(bg_settings2, (0, 0))
        else:
            screen.blit(bg_settings3, (0, 0))
        screen.blit(settings_surface, (W // 2 - settings_surface.get_width() // 2, 20))

        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == USEREVENT and e.button == back_button:
                main_menu()
                sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    main_menu()
                    sys.exit()

            if e.type == USEREVENT and e.button == video_button:
                video_settings()
                sys.exit()

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(e)

        for btn in [audio_button, video_button, back_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()

def video_settings():
    global W, H
    global screen

    basic_button = button.Button(W / 2 - (252 / 2), 200, 252, 74, "1200 x 800", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    medium_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, "1500 x 1000", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    FULL_HD_button = button.Button(W / 2 - (252 / 2), 380, 252, 74, "Full HD", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    back_button = button.Button(W / 2 - (252 / 2), 470, 252, 74, "Back", 'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_settings, (0, 0))
        elif W == 1600:
            screen.blit(bg_settings2, (0, 0))
        else:
            screen.blit(bg_settings3, (0, 0))
        screen.blit(video_settings_surface, (W // 2 - video_settings_surface.get_width() // 2, 20))

        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == USEREVENT and e.button == back_button:
                settings_menu()
                sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    settings_menu()
                    sys.exit()

            if e.type == USEREVENT and e.button == basic_button:
                W, H = 1280, 800
                screen = display.set_mode((W, H))
                settings_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == medium_button:
                W, H = (1600, 1000)
                screen = display.set_mode((W, H))
                settings_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == FULL_HD_button:
                W, H = (1920, 1200)
                screen = display.set_mode((W, H), FULLSCREEN)
                settings_menu()
                sys.exit()

            for btn in [basic_button, medium_button, FULL_HD_button, back_button]:
                btn.handle_event(e)

        for btn in [basic_button, medium_button, FULL_HD_button, back_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()

def help():
    global W, H
    back_button1 = button.Button(W / 2 - (252 / 2), H - 100, 252, 74, "Back", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_help, (0, 0))
        elif W == 1600:
            screen.blit(bg_help2, (0, 0))
        else:
            screen.blit(bg_help3, (0, 0))
        screen.blit(help_surface, (W // 2 - help_surface.get_width() // 2, 20))

        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == USEREVENT and e.button == back_button1:
                main_menu()
                sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    main_menu()
                    sys.exit()

            for btn in [back_button1]:
                btn.handle_event(e)

        back_button1.draw(screen)
        back_button1.check_hover(mouse.get_pos())
        display.flip()


def new_game():
    global W, H
    back_button2 = button.Button(W - 272, H - 100, 252, 74, "Back", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    hint_button = button.Button(W - 272, H - 200, 252, 74, "Hint", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    scroll_down_button = button.Button(W - 272, H - 300, 252, 74, "Scroll Down", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_play, (0, 0))
            screen.blit(bg_play_rect, (0, 0))
        elif W == 1600:
            screen.blit(bg_play2, (0, 0))
            screen.blit(bg_play_rect2, (0, 0))
        else:
            screen.blit(bg_play3, (0, 0))
            screen.blit(bg_play_rect3, (0, 0))

        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == USEREVENT and e.button == back_button2:
                main_menu()
                sys.exit()

            for btn in [back_button2, hint_button, scroll_down_button]:
                btn.handle_event(e)

        for btn in [back_button2, hint_button, scroll_down_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()


if __name__ == '__main__':
    main_menu()
quit()
