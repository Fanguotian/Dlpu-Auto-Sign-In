# coding=UTF-8
from selenium import webdriver
from lxml import etree
from aip import AipOcr
from PIL import Image
import requests
import image
import time
import random
import string
import sys
import os

# 是否需要server酱微信推送
notification = 0

try:
    key = os.environ["key"]
except:
    pass

try:
    user = os.environ["username"]
    pwd = os.environ["password"]
    location = os.environ["location"]
except:
    print("参数不完整或错误，请检查用户名、密码和地点是否正确填写")
    exit(1)

# 适配 Github Actions，否则出错
options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')
options.add_argument("--disable-extensions");
options.add_argument("--disable-gpu");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--no-sandbox");
options.add_argument("--headless");
browser = webdriver.Chrome(options=options)
browser.set_window_size(1200, 2000)

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

# 实际上直接发送请求是最好的，根本用不到selenium，否则网页只要有一点修改就会签到失败
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
time.sleep(10)

# 检查是否签到成功
try:
    browser.switch_to.alert.accept()
except:
    pass
browser.get("https://www.dxever.com/fei/delete/ncp/history.html")
browser.execute_script("""
    (function () {
        var y = 0;
        var step = 100;
        window.scroll(0, 0);
        function f() {
            if (y < document.body.scrollHeight) {
                y += step;
                window.scroll(0, y);
                setTimeout(f, 10000);
            } else {
                window.scroll(0, 0);
                document.title += "scroll-done";
            }
        }
        setTimeout(f, 1000);
    })();
""")
time.sleep(1)

# 使用百度 OCR API 识别签到历史网页，若网页中有“今天”两个字，说明签到成功
# 每日5万免费调用次数
APP_ID = '18692624'
API_KEY = 'MdLFdybWVAsvea70co4BMGxW'
SECRET_KEY = 'IKY0qvDkHGiodOHogc3PqoE07uFXt4Mt'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

browser.save_screenshot("num.png")
with open (r'num.png','rb') as file:
    image = file.read()
    text = client.basicAccurate(image)
    if '今天' in str(text):
        print("签到成功")
        if notification == 1:
            api = 'https://sc.ftqq.com/' + key + '.send'
            title = "签到成功"
            content = "主人，签到成功啦！"
            data = {
               "text" : title,
               "desp" : content
            }
            req = requests.post(api, data = data)
            print("推送成功，假如没有收到推送，请检查key是否正确")
        exit(0)
    else:
        print("签到失败")
        if notification == 1:
            api = 'https://sc.ftqq.com/' + key + '.send'
            title = "签到失败"
            content = "签到失败，请检查发生了什么。若程序有Bug，请提issues"
            data = {
               "text" : title,
               "desp" : content
            }
            req = requests.post(api, data = data)
            print("推送成功，假如没有收到推送，请检查key是否正确")
        exit(1)
