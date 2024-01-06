# Import required modules
import random


class RandomColorGenerator:

    # Randomly set the RGB color
    @staticmethod
    def random_color_generator():
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        # Save colours in the immutable tuple so that there is data integrity and colours never change
        random_color = (r, g, b)
        return random_color
