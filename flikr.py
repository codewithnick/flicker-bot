import os
import urllib
from urllib.request import urlretrieve
from selenium import webdriver
import traceback
import time

driver = webdriver.Chrome('chromedriver')

time.sleep(0.5)
i=0
if(not os.path.exists('website1/database.xlsx')):
    time.sleep(5)
    from openpyxl import Workbook
    book = Workbook()
    sheet = book.active
    sheet['B27']='Title'
    sheet['C27']='Description'
    sheet['D27']='Imageurl'
    sheet['E27']='Price'
else:
    book = openpyxl.load_workbook('database.xlsx')
    sheet = book.active
row=int(sheet.dimensions.split(':')[1][1:])+1

while True:
    #x=input("ente link")
    try:
        try:
            driver.get("https://www.surreyhillsflowerdelivery.com.au/surrey-hills-flowers/white-delight-533589p.asp")
            i+=1
            title = driver.find_element_by_id("headline").text
            desc = driver.find_element_by_id("product-info").text
            imgurl= driver.find_element_by_id("original")
            price = driver.find_element_by_id("ProductPriceLabel0").text
            print(title,desc,imgurl,price)
            exit()
            url=driver.find_element_by_xpath(imgurl).get_attribute('src')
            if not os.path.exists('website1/image'):
                os.makedirs('website1/image')
            path='website1/images/'+str(i)+".jpeg"
            print('downloading from ',url)
            print('saving as '+str(i)+'.jpeg')
            urlretrieve(url,filename=path)#save image
            time.sleep(0.5)
        except:
            pass
    except:
        print('a unexpected error has occured or you have reached end of page')
        traceback.print_exc()















