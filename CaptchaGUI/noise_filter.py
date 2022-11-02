from operator import itemgetter
from PIL import Image
import pytesseract
NAME = "0154."
IMAGE = (Image.open(NAME+'png')).convert("P")

def get_color_frequency():
    """
    finds and returns the most frequent 5 pixel colors in the image
    """
    pixel_values = IMAGE.histogram()
    values = {}
    for i in range(256):
        values[i] = pixel_values[i]
    return(sorted(values.items(), key=itemgetter(1), reverse=True)[:5])

def get_text_color():
    """
    returns the desires color
    """
    frequent_colors = get_color_frequency()
    return(frequent_colors[2][0])

def make_filtered_image_first_round():
    """
    creates a version of the image that only has the same pixel color used in the text
    """
    filtered_image = Image.new("P",IMAGE.size,255)
    temp = {}
    text_color = get_text_color()
    for x in range(IMAGE.size[1]):
        for y in range(IMAGE.size[0]):
            pixel = IMAGE.getpixel((y,x))
            temp[pixel] = pixel
            if pixel == text_color:
                filtered_image.putpixel((y,x),255)
            else:
                filtered_image.putpixel((y,x),0)
    filtered_image.save(NAME + 'round1.gif')



def get_neighbors(x=int,y=int):
    neighbors = []
    indexes = [(0,1),(1,0),(0,-1),(-1,0)]
    for index in indexes:
        neighbors.append([index[0] + x,index[1]+y])
    return neighbors

    
def make_filtered_image_second_round():
    raise NotImplementedError
    filtered_image = Image.new("P",IMAGE.size,0)
    im = Image.open(NAME + 'round1.gif')
    #first_degree_neighbors = []
    #second_degree_neighbors = []
    for _ in range(25):
        for x in range(im.size[1] - 2):
            for y in range(im.size[0] - 2):
                count = 0
                flag = False
                if im.getpixel((y,x)) == 0:
                    while True:
                        if count > 2:
                            break
                        elif im.getpixel((y,x+count)) == 0:
                            count+=1
                        else:    
                            while count > 0:
                                filtered_image.putpixel((y,x+count),255)
                                flag = True
                                count-=1
                        if flag:
                            break
                    count = 0
                    flag = False
                    while True:
                        if count > 2:
                            break
                        elif im.getpixel((y+count,x)) == 0:
                            count+=1
                        else:    
                            while count > 0:
                                filtered_image.putpixel((y+count,x),255)
                                flag = True
                                count-=1
                        if flag:
                            break
                else:
                    filtered_image.putpixel((y,x),255)
    filtered_image.save(NAME + 'round2.gif')

                               
def solve():
    raise NotImplementedError
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    return pytesseract.image_to_string('test.png')

