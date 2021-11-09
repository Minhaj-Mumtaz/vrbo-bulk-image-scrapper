from selenium import webdriver
import time
from PIL import Image
import urllib
import requests

print('\n\nVRBO Image converter from webp to png and download all the pictures one by one')

url = input('Enter vrobo url: ')

path = input('Provide the path where you want images to download: ')

path.replace('"\"','"\\"')

imageRange = int(input('Input the total number of images: '))

driver = webdriver.Chrome(executable_path="C:\\Users\\Lenovo X1 Carbon\\Documents\\Business\\App Development\\VRBO-Scrapper\\vrbo-bulk-image-scrapper\\chromedriver.exe")
driver.get(url)

images = driver.find_element_by_class_name('pdp-layout__top-content')

images.find_element_by_xpath('.//*[@id="photos"]')
images.click()

time.sleep(2)
button = driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/div[2]/button')

for image in range(imageRange):
    

    if (image+1) == 2 or (image+1) == 1:
        img = driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/ol/li['+str(image+1)+']/img')
    elif image == imageRange-2:
        img = driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/ol/li[4]/img')
    elif image == imageRange-1:
        img = driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/ol/li[5]/img')
    else:
        try:
            driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/ol/li[3]/img')
        except:
            print('Video is here')
            image=image+1
            button.click()
            time.sleep(1)
        
        img = driver.find_element_by_xpath('.//*[@id="photos"]/div[2]/div[2]/ol/li[3]/img')

    src = img.get_attribute('src')
    im =  Image.open(requests.get(src, stream=True).raw).convert("RGB")
    im.save(path+"\\"+str(image+1) +".png","png")
    button.click()
    time.sleep(1)

driver.quit()
