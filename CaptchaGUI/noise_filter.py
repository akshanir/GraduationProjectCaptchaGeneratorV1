from PIL import Image
from operator import itemgetter
IMAGE = (Image.open("out.png")).convert("P")
def get_color_frequency():
    his = IMAGE.histogram()
    values = {}
    for i in range(256):
        values[i] = his[i]
    return(sorted(values.items(), key=itemgetter(1), reverse=True)[:5])

def get_text_color():
    frequent_colors = get_color_frequency()
    return(frequent_colors[2][0])

def make_filtered_image():
    im2 = Image.new("P",IMAGE.size,255)
    print(IMAGE.size)
    temp = {}
    color1 = get_text_color()
    for x in range(IMAGE.size[1]):
        for y in range(IMAGE.size[0]):
            pix = IMAGE.getpixel((y,x))
            temp[pix] = pix
            if pix == color1:
                im2.putpixel((y,x),0)
            else:
                im2.putpixel((y,x),255)
    im2.save("output.gif")

    
make_filtered_image()
        