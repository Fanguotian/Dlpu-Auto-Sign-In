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
    user = os.environ["userName"]
    pwd = os.environ["password"]
    isWeekLogin = os.environ["isWeekLogin"]
except:
    print("参数不完整或错误，请检查用户名、密码和地点是否填写")

loginSession = requests.session()
ua = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
header = {
    'User-Agent': ua,
}
postLoginUrl = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/emapfunauth/loginValidate.do"
postLoginData = {
    "userName": user,
    "password": pwd,
    "isWeekLogin":isWeekLogin
}
loginResponse = loginSession.post(postLoginUrl, data = postLoginData, headers = header)
if "200" in str(loginResponse.text):
    token = str(loginResponse.text).split('"')
    signInSession = requests.session()
    postSignInUrl = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/xsyqxxsjapp/mrbpa/saveMrbpa.do"
    postSignInData = {
        "data" : "{'ZYDM': '0103','GJDQ': '156','SFDFHB_DISPLAY': '否','SFJCQZ': '0','SFZJH': '441723199802222411','DWDM': '015','SFFRHKS': '0','JQQK_DISPLAY': '正常','JTCYJKZK_DISPLAY': ''','SZDQ': '441702','SZDQ_DISPLAY': '广东省/阳江市/江城区','SFQGJCHB_DISPLAY': '否','ZYDM_DISPLAY': '软件工程','MRSZDQ1': '441704','SFQZHYS': '0','JJLXRDH': '13025645385','XXDZ': '广东省阳江市江城区石湾北路146号','SFBGL_DISPLAY': '否','XLZK_DISPLAY': '','TW': '36','XBDM': '1','JTXXDZ_DISPLAY': '广东省/阳江市/阳东区','LXDH': '13827623376','SFFRHKS_DISPLAY': '否','JQQK': 'zc','XH': '1701030031','BJDM_DISPLAY': '17软件01','SFBGL': '0','XM': '范国添','SFJZ_DISPLAY': '','SFJCQZ_DISPLAY': '否','SFQGJCHB': '0','TBSJ': '2020-07-04','JTXXDZ': '441704','MRSZDQ_DISPLAY': '广东省/阳江市/阳东区','JJLXRJG_DISPLAY': '广东省/阳江市/阳东区','MRXXDZ1': '广东省阳江市阳东区北惯镇两安村7巷7号','BJDM': '01031701','SFDFHB': '0','SFQZHYS_DISPLAY': '否','JJLXRJG': '441704','JJLXR': '洪小凤'','MRSZDQ1_DISPLAY': '广东省/阳江市/阳东区','DWDM_DISPLAY': '信息技术学院','GJDQ_DISPLAY': '中国','BRJKZT_DISPLAY': '','XBDM_DISPLAY': '男','XZNJ': '2017','MRSZDQ': '441704','isToday': true,'GCKSRQ': '','GCJSRQ': '','DFHTJHBSJ': '','SFFRHKSQKSM': '','SFQZHYSQKSM': ''','SFQGJCHBSQKSM': '','SFJCQZQKSM': '','SFBGLQKSM': '','WID': '4db77cfd035140719e11df6e2397ac86'}"
    }
    signInResponse = signInSession.post(postSignInUrl, data = postSignInData, headers = header)
    if "success" in str(signInResponse.validate):
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
