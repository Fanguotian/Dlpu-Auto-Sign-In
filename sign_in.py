# coding=UTF-8
import requests,time,os
from http import cookiejar
from lxml import etree

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
    print("参数不完整或错误，请检查用户名、密码和地点是否填写")

loginSession = requests.session()
ua = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
header = {
    'User-Agent': ua,
}
postLoginUrl = "https://www.dxever.com/Wxminiprog/Disease/login"
postLoginData = {
    "studno": user,
    "password": pwd,
}
loginResponse = loginSession.post(postLoginUrl, data = postLoginData, headers = header)
if "200" in str(loginResponse.text):
    token = str(loginResponse.text).split('"')
    signInSession = requests.session()
    postSignInUrl = "https://www.dxever.com/Wxminiprog/Disease/addLog"
    postSignInData = {
        "token": token[-2],
        "curlocation": location,
        "goout": "0",
        "hp": "0",
        "ncp": "0",
        "isncp": "0",
        "touchncp": "0",
        "hubei": "0",
        "ps": "",
    }
    signInResponse = signInSession.post(postSignInUrl, data = postSignInData, headers = header)
    if "200" in str(signInResponse.content):
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
    else:
        print("签到失败，可能已签到过")
        if notification == 1:
            api = 'https://sc.ftqq.com/' + key + '.send'
            title = "签到失败"
            content = "签到失败，请检查是否签到成功，并查看 Github Actions 日志。若程序有Bug，请提issues"
            data = {
               "text" : title,
               "desp" : content
            }
            req = requests.post(api, data = data)
            print("推送成功，假如没有收到推送，请检查key是否正确")
else:
    print("用户名或者密码错误")
