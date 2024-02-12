import os
import shutil
from PIL import Image


class folders:
    def create_folder():  # создание временной папки
        shutil.rmtree(os.path.abspath('temp_folder'))
        os.mkdir('temp_folder')

    def split_image_into_squares(image_path, save_dir, num_squares):  # алгоритм разбития
        global square_size
        image = Image.open(image_path)
        width, height = image.size
        square_size = min(width, height) // num_squares

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for y in range(1, num_squares + 1):
            for x in range(num_squares):
                left = x * square_size + 200
                upper = y * square_size - 200
                right = left + square_size
                lower = upper + square_size
                square = image.crop((left, upper, right, lower))
                square.save(os.path.join(save_dir, f"square_{num_squares * (y - 1) + x + 1}.jpg"))

    def make_sqares(sq1, current_image):  # создание мозаики
        image_path = f"images/images_to_pazzle/{current_image}.jpg"
        save_dir = "temp_folder"
        num_squares = sq1
        folders.split_image_into_squares(image_path, save_dir, num_squares)

    def main(sq, image):
        folders.create_folder()
        folders.make_sqares(sq, image)
