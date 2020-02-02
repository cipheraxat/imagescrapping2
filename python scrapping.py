# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:40:38 2020
flipkart pantry
"""
from selenium import webdriver
import urllib.request 



c2w_driver = webdriver.Chrome('C:/webdriver/chromedriver.exe')
c2w_driver.get('https://www.flipkart.com/food-nutrition/modern-pantry~brand/pr?sid=7jv')
i=1
while(i!=5):
    
    i=str(i)
    im=c2w_driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div['+i+']/div/a[1]/div[1]/div/div/img')
                                         
                          
    src = im.get_attribute('src')

    nam="captcha"+i+".png"
    i=int(i)
    i=i+1
    print(i)
    urllib.request.urlretrieve(src, nam)

c2w_driver.close()
