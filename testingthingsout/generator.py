import numbers
import string
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from random import choice

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_random_string(length=int):
    str = ''
    for i in range(length):
        str += choice(numbers)
    return str

def get_captcha_image(length=int):
    image = ImageCaptcha(160, 60, fonts=['\assets\fonts\OpenSans-Regular.ttf'])
    s = get_random_string(length)
    image.write(s, 'out.png')
    return s
    # print(s)
    # return image.generate(s)
    # data = image.generate(s)
