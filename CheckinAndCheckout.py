'''
Release note:
    Author:brook.huang@fengsui.com.tw
    ver.1&2 relese date:20180516
Ver.1 This application is used to auto check in and check out.
Ver.2 Add dandom delay funtion and intorduce ID and password from file.
Note:
    20480516 currently, this applicatio needs to company with windows' task
    schedular to execute. There is one thing shoudl be mentioned, the
    chromedriver.exe should be placed in the same folder.    
'''


import time
import os
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#ActionChains is used to perform right click
import random
file_path=os.path.abspath('IDAndPWD.txt')
print(file_path)

try:
    input_file=open(file_path,'r')
except FileNotFoundError:
    print("File Not Found")
finally:    
    IAP=input_file.read().split(';')
    print(IAP[0],IAP[1]) #used to debug
    x=random.randint(0,100)
    print(x)
    time.sleep(x)
    driver = webdriver.Chrome()
    driver.get("https://pro.104.com.tw/hrm/psc/home.action")    
    driver.find_element_by_id("email").send_keys(str(IAP[0]))
    driver.find_element_by_id("pwd").send_keys(str(IAP[1]))
    before_login_url=driver.current_url #used to debug
    driver.find_element_by_id("submit").click()
time.sleep(5)
after_login_url=driver.current_url #used to debug
if before_login_url == after_login_url: #used to debug
    print("unchanged") #used to debug
else: #used to debug
    print("changed") #used to debug
    driver.get("https://pro.104.com.tw/hrm/psc/home.action") 
    redirection_url=driver.current_url
    print(redirection_url)
time.sleep(10)
#time.sleep(10) #used to debug
driver.find_element_by_id("punchCardBtn").click()
driver.quit()
input_file.close()