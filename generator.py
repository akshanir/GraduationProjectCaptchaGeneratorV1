from captcha.image import ImageCaptcha
from random import choice

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_random_string(length=int):
    # Generates a variable length string consisting of 0-9 digits
    str = ''
    for i in range(length):
        str += choice(numbers)
    return str

def get_captcha_image(length=int):
    # Generates a captcha image and writes it on disk, returns its solution
    image = ImageCaptcha(160, 60, fonts=['\assets\fonts\OpenSans-Regular.ttf'])
    s = get_random_string(length)
    image.write(s, 'out.png')
    return s
