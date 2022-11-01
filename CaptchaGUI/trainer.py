from generator import get_captcha_image
def generate_set(set_size=int,text_length=4):
    """
    generates a set of captcha images, their number is determined by the set_size parameter while text_length determines the
    length of the text in the iamges. the images' solutions will be saved on a text file in the format ID:Solution.
    the images and the file can be found in the trainset directory.
    """
    with open ("trainset/list.txt","w") as file:
        for ID in range(set_size):
            file.write(str(ID) + ":" + get_captcha_image(text_length,"trainset/") +"\n")
