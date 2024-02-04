import os
from PIL import Image


class folders:
    global W
    global H
    def create_folder():  # создание временной папки
        if not os.path.isdir('temp_folder'):
            os.mkdir('temp_folder')
        else:
            pass

    def split_image_into_squares(image_path, save_dir, num_squares):  # алгоритм разбития
        image = Image.open(image_path)
        width, height = image.size
        square_size = min(width, height) // num_squares

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for y in range(num_squares):
            for x in range(num_squares):
                left = x * square_size
                upper = y * square_size
                right = left + square_size
                lower = upper + square_size
                square = image.crop((left, upper, right, lower))
                square.save(os.path.join(save_dir, f"square_{x}_{y}.jpg"))

    def make_sqares(sq1):  # создание мозаики
        image_path = "images/images_to_pazzle/file.png"
        save_dir = "temp_folder"
        num_squares = sq1
        folders.split_image_into_squares(image_path, save_dir, num_squares)

    def main(sq):
        folders.create_folder()
        folders.make_sqares(sq)
