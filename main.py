from pygame import *
from scripts import button
from scripts import temp_folder
import sys
import time
import random
import os
from PIL import Image

difficulty = {1: 'easy (4 * 4)', 2: 'normal (5 * 5)', 3: 'hard (8 * 8)',
              4: 'very hard (16 * 16)'}  # стартовые настройки
dif = {1: 4, 2: 5, 3: 8, 4: 16}
left_top_angles = {}
count = 1
# image_number = 0

init()
W, H = 1280, 800
screen = display.set_mode((W, H))
display.set_caption('PuzzleGame')

icon = image.load('images/icon/icon.png')
display.set_icon(icon)
# изображения
bg_main = image.load('images/backGround/bg_main.png')
bg_settings = image.load('images/backGround/bg_settings.png')
bg_help = image.load('images/backGround/bg_help.png')
bg_play = image.load('images/backGround/bg_play2.png')
bg_play_rect = image.load('images/backGround/bg_play_Rect.png')
bg_play_rect_PIL = Image.open('images/backGround/bg_play_Rect.png')

bg_main2 = image.load('images/backGround/bg_main2.png')
bg_settings2 = image.load('images/backGround/bg_settings2.png')
bg_help2 = image.load('images/backGround/bg_help2.png')
bg_play2 = image.load('images/backGround/bg_play3.png')
bg_play_rect2 = image.load('images/backGround/bg_play_Rect2.png')
bg_play_rect2_PIL = Image.open('images/backGround/bg_play_Rect2.png')

bg_main3 = image.load('images/backGround/bg_main3.png')
bg_settings3 = image.load('images/backGround/bg_settings3.png')
bg_help3 = image.load('images/backGround/bg_help3.png')
bg_play3 = image.load('images/backGround/bg_play4.png')
bg_play_rect3 = image.load('images/backGround/bg_play_Rect3.png')
bg_play_rect3_PIL = Image.open('images/backGround/bg_play_Rect3.png')

messed_up_1_1 = image.load('images/you_messed_up/haha_you_messed_up_1_1.png')  # 1 сек до продолжения 1280 x 800
messed_up_1_2 = image.load('images/you_messed_up/haha_you_messed_up_1_2.png')  # 2 сек до продолжения 1280 x 800

messed_up_2_1 = image.load('images/you_messed_up/haha_you_messed_up_2_1.png')  # 1 сек до продолжения 1600 x 1000
messed_up_2_2 = image.load('images/you_messed_up/haha_you_messed_up_2_2.png')  # 2 сек до продолжения 1600 x 1000

messed_up_3_1 = image.load('images/you_messed_up/haha_you_messed_up_3_1.png')  # 1 сек до продолжения 1920 x 1200
messed_up_3_2 = image.load('images/you_messed_up/haha_you_messed_up_3_2.png')  # 2 сек до продолжения 1920 x 1200

PuzzleGame_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
PuzzleGame_surface = PuzzleGame_txt.render('PuzzleGame', True, (230, 143, 85))
main_font = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 50)
main_font2 = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 40)
font_to_warning = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 35)
font_to_warning2 = font.Font('Fonts/Oswald-VariableFont_wght.ttf', 20)

settings_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
settings_surface = settings_txt.render('Settings', True, (230, 143, 85))

video_settings_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
video_settings_surface = video_settings_txt.render('Video Settings', True, (230, 143, 85))

image_choose_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
image_choose_surface = image_choose_txt.render('Choose Image', True, (230, 143, 85))

help_txt = font.Font('Fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf', 100)
help_surface = help_txt.render('Help', True, (230, 143, 85))

help_description_surface1 = main_font2.render('1. Choose difficulty by clicking on the second button in main menu.',
                                              True, (196, 2, 21))
help_description_surface2 = main_font2.render('2. Choose comfortable window size in settings/video.', True,
                                              (196, 2, 21))
help_description_surface3 = main_font2.render('3. Click play button.', True, (196, 2, 21))
help_description_surface4 = main_font2.render(
    '4. Type position of the picture by typing on keyboard, click check placement button.', True, (196, 2, 21))
help_description_surface5 = main_font2.render(
    '5. Click scroll ddwn button if you cant imagine where position of the picture will be.', True, (196, 2, 21))
help_description_surface6 = main_font2.render('6. Enjoy!', True, (196, 2, 21))

pictures_to_puzzle = ['first_image', 'second_image', 'third_image', 'forth_image', 'fifth_image']
image_to_puzzle_current = pictures_to_puzzle[0]


def diff(df_bt):  # сложности
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


def main_menu():  # менюшка
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


def settings_menu():  # меню настроек
    global W
    pazzle_image = button.Button(W / 2 - (252 / 2), 200, 252, 74, "Puzzle image", 'images/buttons/static_button.png',
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

            if e.type == USEREVENT and e.button == pazzle_image:
                image_choose()
                sys.exit()

            for btn in [pazzle_image, video_button, back_button]:
                btn.handle_event(e)

        for btn in [pazzle_image, video_button, back_button]:
            btn.draw(screen)
            btn.check_hover(mouse.get_pos())
        display.flip()


def video_settings():
    global W, H
    global screen
    # настройки видео
    basic_button = button.Button(W / 2 - (252 / 2), 200, 252, 74, "1280 x 800", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    medium_button = button.Button(W / 2 - (252 / 2), 290, 252, 74, "1600 x 1000", 'images/buttons/static_button.png',
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


def image_choose():
    global W, H, image_to_puzzle_current
    global screen
    # выбор изображения
    if W == 1280:
        back_button = button.Button(W - 272, H - 94, 252, 74, "Back", 'images/buttons/static_button.png',
                                    'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        first_image_button = button.Button(40, 310, 150, 60, "first image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        second_image_button = button.Button(240, 310, 150, 60, "second image", 'images/buttons/static_button.png',
                                            'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        third_image_button = button.Button(440, 310, 150, 60, "third image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        forth_image_button = button.Button(640, 310, 150, 60, "forth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        fifth_image_button = button.Button(840, 310, 150, 60, "fifth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    elif W == 1600:
        back_button = button.Button(W - 272, H - 94, 252, 74, "Back", 'images/buttons/static_button.png',
                                    'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        first_image_button = button.Button(40, 310, 150, 60, "first image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        second_image_button = button.Button(304, 310, 150, 60, "second image", 'images/buttons/static_button.png',
                                            'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        third_image_button = button.Button(568, 310, 150, 60, "third image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        forth_image_button = button.Button(832, 310, 150, 60, "forth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        fifth_image_button = button.Button(1096, 310, 150, 60, "fifth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    else:
        back_button = button.Button(W - 272, H - 94, 252, 74, "Back", 'images/buttons/static_button.png',
                                    'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        first_image_button = button.Button(40, 310, 150, 60, "first image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        second_image_button = button.Button(368, 310, 150, 60, "second image", 'images/buttons/static_button.png',
                                            'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        third_image_button = button.Button(696, 310, 150, 60, "third image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        forth_image_button = button.Button(1024, 310, 150, 60, "forth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
        fifth_image_button = button.Button(1352, 310, 150, 60, "fifth image", 'images/buttons/static_button.png',
                                           'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')

    display.update()
    running = True
    while running:
        screen.fill((0, 0, 0))
        if W == 1280:
            screen.blit(bg_settings, (0, 0))
            for i in range(len(pictures_to_puzzle)):
                image_to_load = image.load(f'images/images_to_pazzle_preview/{pictures_to_puzzle[i]}.png')
                screen.blit(image_to_load, (40 + 200 * i, 200))
        elif W == 1600:
            screen.blit(bg_settings2, (0, 0))
            for i in range(len(pictures_to_puzzle)):
                image_to_load = image.load(f'images/images_to_pazzle_preview/{pictures_to_puzzle[i]}.png')
                screen.blit(image_to_load, (40 + 264 * i, 200))
        else:
            screen.blit(bg_settings3, (0, 0))
            for i in range(len(pictures_to_puzzle)):
                image_to_load = image.load(f'images/images_to_pazzle_preview/{pictures_to_puzzle[i]}.png')
                screen.blit(image_to_load, (40 + 328 * i, 200))
        screen.blit(image_choose_surface, (W // 2 - image_choose_surface.get_width() // 2, 20))

        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == USEREVENT and e.button == back_button:
                settings_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == first_image_button:
                image_to_puzzle_current = pictures_to_puzzle[0]
                main_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == second_image_button:
                image_to_puzzle_current = pictures_to_puzzle[1]
                main_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == third_image_button:
                image_to_puzzle_current = pictures_to_puzzle[2]
                main_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == forth_image_button:
                image_to_puzzle_current = pictures_to_puzzle[3]
                main_menu()
                sys.exit()

            if e.type == USEREVENT and e.button == fifth_image_button:
                image_to_puzzle_current = pictures_to_puzzle[4]
                main_menu()
                sys.exit()

            for btn in [back_button, first_image_button, second_image_button, third_image_button,
                        forth_image_button, fifth_image_button]:
                btn.handle_event(e)

        for btn in [back_button, first_image_button, second_image_button, third_image_button,
                    forth_image_button, fifth_image_button]:
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
        screen.blit(help_description_surface1, (W // 2 - help_description_surface1.get_width() // 2, 140))
        screen.blit(help_description_surface2, (W // 2 - help_description_surface2.get_width() // 2, 220))
        screen.blit(help_description_surface3, (W // 2 - help_description_surface3.get_width() // 2, 300))
        screen.blit(help_description_surface4, (W // 2 - help_description_surface4.get_width() // 2, 380))
        screen.blit(help_description_surface5, (W // 2 - help_description_surface5.get_width() // 2, 460))
        screen.blit(help_description_surface6, (W // 2 - help_description_surface6.get_width() // 2, 540))

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


def collecting_angles(left1, top1):
    image_number = 0
    for y in range(0, dif[count]):  # отступ top
        for x in range(0, dif[count]):  # отступ left
            left_top_angles[f'{image_number}'] = (left1 + x * temp_folder.square_size,
                                                  top1 + y * temp_folder.square_size)
            image_number += 1


def new_game():
    global W, H, count, image_to_puzzle_current, lose
    text = ''
    index = 0
    count_use = 0
    used = False
    lose = False
    asd = False
    text_surface = main_font.render(text, True, (26, 117, 47))
    temp_folder.folders.main(dif[count], image_to_puzzle_current)
    os.startfile(os.path.abspath(f'images/images_to_pazzle/{image_to_puzzle_current}.jpg'))
    bool_type = {}
    back_button2 = button.Button(W - 272, H - 100, 252, 74, "Back", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    hint_button = button.Button(W - 272, H - 200, 252, 74, "Hint", 'images/buttons/static_button.png',
                                'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    scroll_down_button = button.Button(W - 272, H - 300, 252, 74, "Scroll Down", 'images/buttons/static_button.png',
                                       'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    check_button = button.Button(W - 272, H - 400, 252, 74, "Check placement", 'images/buttons/static_button.png',
                                 'images/buttons/hovered_button.png', 'sound_effects/button_clicked.mp3')
    index_list = []
    for i in range(1, dif[count] * dif[count] + 1):
        index_list.append(i)
    random.shuffle(index_list)
    current_image = image.load(f'temp_folder/square_{index_list[index]}.jpg')
    display.update()
    running = True
    while running:
        if lose:
            screen.fill((0, 0, 0))
            if W == 1280:
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_1_2, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_1_1, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break

            if W == 1600:
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_2_2, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_2_1, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break
            if W == 1920:
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_3_2, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break
                start_time = time.time()
                end_time = 1
                while True:
                    current_time = int(time.time() - start_time)
                    screen.blit(messed_up_3_1, (0, 0))
                    display.flip()
                    if current_time is end_time:
                        lose = False
                        break

        else:
            screen.fill((0, 0, 0))
            if W == 1280:
                screen.blit(bg_play, (0, 0))
                screen.blit(bg_play_rect, (0, 0))  # фон в главном меню
                screen.blit(text_surface, (W - 272, H - 500))
                width, height = bg_play_rect_PIL.size
            elif W == 1600:
                screen.blit(bg_play2, (0, 0))
                screen.blit(bg_play_rect2, (0, 0))
                screen.blit(text_surface, (W - 272, H - 500))
                width, height = bg_play_rect2_PIL.size
            else:
                screen.blit(bg_play3, (0, 0))
                screen.blit(bg_play_rect3, (0, 0))
                screen.blit(text_surface, (W - 272, H - 500))
                width, height = bg_play_rect3_PIL.size

            for i in range(len(bool_type)):
                keys = list(bool_type.keys())
                if bool_type[keys[i]]:
                    image_to_load = image.load(f'temp_folder/square_{bool_type[keys[i]]}.jpg')
                    screen.blit(image_to_load, left_top_angles[str(keys[i] - 1)])
            screen.blit(current_image, (W - 272, 50))
            left = (width - temp_folder.square_size * dif[count]) // 2
            top = (height - temp_folder.square_size * dif[count]) // 2
            for x in range(0, dif[count] + 1):
                draw.line(screen, Color('BLACK'), [left + temp_folder.square_size * x, top],
                          [left + temp_folder.square_size * x, top + temp_folder.square_size * dif[count]], 3)
            for y in range(0, dif[count] + 1):
                draw.line(screen, Color('BLACK'), [left, top + temp_folder.square_size * y],
                          [left + temp_folder.square_size * dif[count], top + temp_folder.square_size * y], 3)
            collecting_angles(left, top)
            for i in range(1, dif[count] * dif[count] + 1):
                number_surfaces = font_to_warning2.render(f'{i}', True, (0, 0, 0))
                screen.blit(number_surfaces, (5 + left_top_angles[f'{i - 1}'][0], left_top_angles[f'{i - 1}'][1]))
            for e in event.get():
                if e.type == QUIT:
                    running = False

                if e.type == USEREVENT and e.button == back_button2:
                    main_menu()
                    sys.exit()

                if e.type == USEREVENT and e.button == check_button:
                    count_use = 0
                    used = False
                    text = ''
                    text_surface = font_to_warning.render(text, True, Color('RED'))
                    bool_type_copy = bool_type
                    keys = list(bool_type_copy.keys())
                    for i in range(len(keys)):
                        if bool_type_copy[keys[i]] != keys[i]:
                            del bool_type[keys[i]]
                            lose = True

                if e.type == KEYDOWN:
                    if e.key == K_BACKSPACE:
                        text = text[0:-1]
                        text_surface = main_font.render(text, True, (26, 117, 47))
                    elif e.key == K_RETURN:
                        if text == '':
                            text = 'please type digit'
                            text_surface = font_to_warning.render(text, True, Color('RED'))
                            text = ''
                        elif int(text) <= dif[count] * dif[count] and (int(text) > 0):
                            for i in list(bool_type.keys()):
                                if index_list[index] == bool_type[i]:
                                    count_use += 1
                                if count_use >= 1:
                                    used = True
                            if int(text) in list(bool_type.keys()):
                                text = 'cell already used'
                                text_surface = font_to_warning.render(text, True, Color('RED'))
                                text = ''
                            elif not used:
                                bool_type[int(text)] = index_list[index]
                                text = ''
                                text_surface = main_font.render(text, True, (26, 117, 47))
                            else:
                                text = 'image already used'
                                text_surface = font_to_warning.render(text, True, Color('RED'))
                                text = ''
                    elif e.key == K_z:
                        if bool_type:
                            del bool_type[list(bool_type.keys())[-1]]
                    else:
                        if e.unicode.isdigit():
                            text += e.unicode
                            text_surface = main_font.render(text, True, (26, 117, 47))

                if e.type == USEREVENT and e.button == scroll_down_button:
                    count_use = 0
                    used = False
                    text = ''
                    text_surface = font_to_warning.render(text, True, Color('RED'))
                    if index + 1 >= len(index_list):
                        index = 0
                    else:
                        index += 1
                    current_image = image.load(f'temp_folder/square_{index_list[index]}.jpg')

                if e.type == USEREVENT and e.button == hint_button:
                    text = str(index_list[index])
                    text_surface = main_font.render(text, True, (26, 117, 47))

                for btn in [back_button2, hint_button, scroll_down_button, check_button]:
                    btn.handle_event(e)

            for btn in [back_button2, hint_button, scroll_down_button, check_button]:
                btn.draw(screen)
                btn.check_hover(mouse.get_pos())
            display.flip()


if __name__ == '__main__':
    main_menu()
quit()
