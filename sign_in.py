# coding=UTF-8
from selenium import webdriver
import time
import random
import string
import sys
import os

try:
    user = os.environ["username"]
    pwd = os.environ["password"]
    location = os.environ["location"]
except:
    print("参数不完整或错误，请检查用户名、密码和地点是否正确填写")
    exit(1)

options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')
options.add_argument("--disable-extensions");
options.add_argument("--disable-gpu");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--no-sandbox");
options.add_argument("--headless");
browser = webdriver.Chrome(options=options)

def LogIn():
    browser.get("https://www.dxever.com/fei/delete/ncp/login.html")
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="box"]/input[1]').send_keys(user)
    browser.find_element_by_xpath('//*[@id="box"]/input[2]').send_keys(pwd)
    browser.find_element_by_xpath('//*[@id="box"]/button').click()
    time.sleep(5)

LogIn()

try:
    browser.find_element_by_xpath('//*[@id="item"]/ul/li[1]/input')
except:
    time.sleep(5)
    LogIn()
    try:
        browser.find_element_by_xpath('//*[@id="item"]/ul/li[1]/input')
    except:
        print("用户名或密码错误")
        exit(1)

browser.find_element_by_xpath('//*[@id="item"]/ul/li[1]/input').send_keys(location)
browser.find_element_by_xpath('//*[@id="item"]/ul/li[2]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[3]/div/input[1]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[4]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[5]/div/input[3]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[6]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[7]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/div/button').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[2]/div[2]/span[2]').click()

try:
    browser.switch_to.alert.accept()
except:
    pass

browser.get("https://www.dxever.com/fei/delete/ncp/history.html")
if "今天" in browser.page_source:
    print("签到成功")
    exit(0)
else:
    print("签到失败")
    exit(1)
