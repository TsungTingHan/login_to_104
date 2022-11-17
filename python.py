from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import os

this_folder = os.path.dirname(os.path.abspath(__file__))
ini_file = os.path.join(this_folder,'config.ini')

config = configparser.ConfigParser()
config.read(ini_file)

user_id = config['user']['user_id']
user_pw = config["user_pw"]["user_pw"]
user_name = config['user']['user_name']

driver = webdriver.Chrome("/Users/louise.han/Documents/test/chromedriver")
driver.get("https://104.com.tw/") 


no_show_again_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"checkbox"))
    )
no_show_again_checkbox.click()

cancel_button = driver.find_element_by_xpath("//*[contains(text(), 'Cancel')]")
cancel_button.click()

login_icon = driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a')
login_icon.click()

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,"username"))
    )
username.send_keys(user_id)

password = driver.find_element_by_id('password')
password.send_keys(user_pw)

login_user_button = driver.find_element_by_id('submitBtn')
login_user_button.click()

username_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/header/div[1]/nav/ul[2]/li[1]/a/span[2]"))
    )
username_icon.click()

my_name = driver.find_element_by_xpath('//*[@id="introjs-1"]/div[1]/div/div[2]/div[1]').text
if my_name == user_name:
    logout_button = driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a')
    logout_button.click()

driver.close()

