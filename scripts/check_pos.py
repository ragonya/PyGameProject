from main import *


dif = {1: 4, 2: 5, 3: 8, 4: 16}
class check:
    global list_images
    global current_image
    global count

    def __init__(self, text):
        self.text = text
        self.current_image = current_image
        self.list_images = list_images
        self.count = count
        self.count2 = ''

    def check_position(self):
        self.count2 = self.list_images.index(self.current_image) + 1
        if self.count != self.count2:
            return False
