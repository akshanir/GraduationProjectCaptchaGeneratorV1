from operator import itemgetter
from captcha_solver import CaptchaSolver
from PIL import Image
import pytesseract
IMAGE = (Image.open("0052.png")).convert("P")
def get_color_frequency():
    """
    finds and returns the most frequent 5 pixel colors in the image
    """
    pixel_values = IMAGE.histogram()
    values = {}
    for i in range(256):
        values[i] = pixel_values[i]
    return(sorted(values.items(), key=itemgetter(1), reverse=True)[:10])

def get_text_color():
    """
    returns the third most frequent color, the first being the background and the second being the extra noise
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
                filtered_image.putpixel((y,x),0)
            else:
                filtered_image.putpixel((y,x),255)
    filtered_image.save("filtered.gif")



def get_neighbors(x=int,y=int):
    neighbors = []
    indexes = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,1)]
    for index in indexes:
        neighbors.append([index[0] + x,index[1]+y])
    return neighbors

    
def make_filtered_image_second_round():
    raise NotImplementedError
    """
    if pixel y(i,j) is black, check neighboring pixels (i+1,j) (i-1,j) (i,j+1) (i,j-1), if a white pixel x is found,
    search for x's neighbors. if one of them such that x != y was black, then turn x black
    """
    im = Image.open("filtered.gif")
    first_degree_neighbors = []
    second_degree_neighbors = []
    for x in range(2,im.size[1]-2):
        for y in range(2,im.size[0]-2):
            pixel = im.getpixel((y,x))
            if pixel ==  0:
                first_degree_neighbors = get_neighbors(x,y)      
                for first_neighbor in first_degree_neighbors:
                    if im.getpixel((first_neighbor[1],first_neighbor[0])) == 255:
                        second_degree_neighbors = get_neighbors(first_neighbor[0],first_neighbor[1])
                        for second_neighbor in second_degree_neighbors:
                            if second_neighbor[0] == x and second_neighbor[1] == y:
                                continue
                            if im.getpixel((second_neighbor[1],second_neighbor[0])) == 0:
                                im.putpixel((first_neighbor[1],first_neighbor[0]),50)
                                flag = True
                                break     
    im.save("filtered.gif")



                            
                
                
def solve():
    raise NotImplementedError


