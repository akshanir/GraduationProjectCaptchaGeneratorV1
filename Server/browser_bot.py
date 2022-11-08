from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import io
from PIL import Image
#from plaything import predict


def download_image(url):
    #browser.save_screenshot('screenshot.png')
    img = browser.find_element(By.ID, 'captcha')
    # cv2.resize(img, )
    img = img.screenshot_as_png
    img_file = io.BytesIO(img)
    #Stores the file in memory and convert to image file using Pillow
    im = Image.open(img_file)

    with open('Captcha.png', 'wb') as file:
      im.save(file, 'png')


    

def solve_Captcha():
    searchBar = browser.find_element(By.ID, "text bar")
    cap = browser.find_element(By.ID, 'captcha')
    src = cap.get_attribute('src')
    download_image(src)
    answer = "bruh"
    # searchBar should be outside the function for time's complexity sack
    time.sleep(0.3)
    searchBar.send_keys(answer)
    time.sleep(0.1)
    searchBar.send_keys(Keys.ENTER)

browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://127.0.0.1:10000')
while True:
  solve_Captcha()
  time.sleep(0.1)

