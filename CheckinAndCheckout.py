'''
Release note:
    Author:brook.huang@fengsui.com.tw

20180516. This application is used to auto check in and check out.
          Add dandom delay funtion and intorduce ID and password from file.
20180524. add IAP[0]=ID
          IAP[1]=PWD
          IAP[2]=random maximum value
          IAP[3]=url
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
file_path=os.path.abspath('SettingInfo.txt')
print(file_path)

try:
    input_file=open(file_path,'r')
except FileNotFoundError:
    print("File Not Found")
finally:    
    IAP=input_file.read().split(';')
    print(IAP[0],IAP[1],IAP[2],IAP[3]) #used to debug  
    x=random.randint(0,int(IAP[2]))
    print(x)
    time.sleep(x)
    driver = webdriver.Chrome()
    driver.get(IAP[3])    
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
    driver.get(IAP[3]) 
    redirection_url=driver.current_url
    print(redirection_url)
time.sleep(10)
#time.sleep(10) #used to debug
driver.find_element_by_id("punchCardBtn").click()
driver.quit()
input_file.close()