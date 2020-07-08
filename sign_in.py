# coding=UTF-8
import requests,time,os
from http import cookiejar
from lxml import etree

# 是否需要server酱微信推送
notification = 1

key = "SCU104265Tcbb1a11f7e3e244dcc30e11152a076545f00497175239"


# try:
#     user = os.environ["userName"]
#     pwd = os.environ["password"]
#     isWeekLogin = os.environ["isWeekLogin"]
# except:
#     print("参数不完整或错误，请检查用户名、密码和地点是否填写")

user = "1701030031"
pwd = "Fan4761520"
isWeekLogin = "false"

now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
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
print("login: %s" % loginResponse.text)
if "success" in str(loginResponse.text):
    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/emaphome/redirect.do?service=%2Fxsdtfw%2Fsys%2Fswmxsyqxxsjapp%2F*default%2Findex.do"
    loginSession.get(url)
    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/emaphome/appShow.do?name=swmxsyqxxsjapp"
    loginSession.get(url)
    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/swpubapp/MobileCommon/getSelRoleConfig.do"
    d = {
        "APPID": "5811260348942403",
        "APPNAME": "swmxsyqxxsjapp"
    }
    data = {
        "data": d
    }
    loginSession.post(url, data)
    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/emappagelog/config/swmxsyqxxsjapp.do"
    loginSession.get(url)

    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/swmxsyqxxsjapp/modules/mrbpa/judgeTodayHasData.do"
    d = {}
    data = {
        "data": d
    }


    r1 = loginSession.post(url, data=data)

    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/swmxsyqxxsjapp/modules/mrbpa/getSetting.do"
    r1 = loginSession.post(url, data=data)
    print("r1:%s" % r1.text)
    wid = json.loads(r1.text).get('data').get('WID')
    print("wid: %s" % wid)
    url = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/swmxsyqxxsjapp/modules/mrbpa/getStuXx.do"
    d = {
        "WID": wid
    }
    data = {
        "data": d
    }
    
    postSignInUrl = "http://xgfx.bnuz.edu.cn/xsdtfw/sys/xsyqxxsjapp/mrbpa/saveMrbpa.do"
    data = {
        "ZYDM": "0103",
        "GJDQ": "156",
        "SFDFHB_DISPLAY": "否",
        "SFZJH": "441723199802222411",
        "DWDM": "015",
        "JQQK_DISPLAY": "正常",
        "JTCYJKZK_DISPLAY": "",
        "SZDQ": "441702",
        "SZDQ_DISPLAY": "广东省/阳江市/江城区",
        "SFQGJCHB_DISPLAY": "否",
        "ZYDM_DISPLAY": "软件工程",
        "MRSZDQ1": "441704",
        "JJLXRDH": "13025645385",
        "XXDZ": "广东省阳江市江城区石湾北路146号",
        "SFBGL_DISPLAY": "否",
        "XLZK_DISPLAY": "",
        "RYLB_DISPLAY": "",
        "XBDM": "1",
        "JTXXDZ_DISPLAY": "广东省/阳江市/阳东区",
        "LXDH": "13827623376",
        "SFFRHKS_DISPLAY": "否",
        "JQQK": "zc",
        "XH": "1701030031",
        "BJDM_DISPLAY": "17软件01",
        "XM": "范国添",
        "SFJZ_DISPLAY": "",
        "SFJCQZ_DISPLAY": "否",
        "JTXXDZ": "441704",
        "MRSZDQ_DISPLAY": "广东省/阳江市/阳东区",
        "JJLXRJG_DISPLAY": "广东省/阳江市/阳东区",
        "MRXXDZ1": "广东省阳江市阳东区北惯镇两安村7巷7号",
        "BJDM": "01031701",
        "SFDFHB": "0",
        "SFQZHYS_DISPLAY": "否",
        "JJLXRJG": "441704",
        "JJLXR": "洪小凤",
        "MRSZDQ1_DISPLAY": "广东省/阳江市/阳东区",
        "DWDM_DISPLAY": "信息技术学院",
        "GJDQ_DISPLAY": "中国",
        "BRJKZT_DISPLAY": "",
        "XBDM_DISPLAY": "男",
        "XZNJ": "2017",
        "TBSJ": now_time,
        "MRSZDQ": "441704",
        "MRXXDZ": "广东省阳江市阳东区北惯镇两安村7巷7号",
        "GCKSRQ": "",
        "GCJSRQ": "",
        "DFHTJHBSJ": "",
        "SFFRHKS": "0",
        "SFFRHKSQKSM": "",
        "SFQGJCHB": "0",
        "SFQGJCHBSQKSM": "",
        "SFJCQZ": "0",
        "SFJCQZQKSM": "",
        "SFQZHYS": "0",
        "SFQZHYSQKSM": "",
        "SFBGL": "0",
        "SFBGLQKSM": "",
        "TW": "36.5"
    }
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    postSignInData = {
        "data": data
    }
    print("data: %s" % postSignInData)
#     signInResponse = signInSession.post(postSignInUrl, data = postSignInData, headers = header)
#     signInResponse = loginSession.post(postSignInUrl, data = postSignInData, headers = header)
    pd = json.dumps(postSignInData)
    signInResponse = loginSession.post(postSignInUrl, data=pd, headers=header)
    print("sign: %s" % signInResponse.text)
    if "成功" in str(signInResponse.text):
        print("签到成功")
        if notification == 1:
            api = 'https://sc.ftqq.com/' + key + '.send'
            title = "签到成功"
            content = signInResponse.text
            data = {
                "text" : title,
                "desp" : content
            }
            req = requests.post(api, data = data)
            print("推送成功，假如没有收到推送，请检查key是否正确")
    else:
        print("签到失败")
        if notification == 1:
            api = 'https://sc.ftqq.com/' + key + '.send'
            title = "签到失败"
            content = signInResponse.text
            data = {
               "text" : title,
               "desp" : content
            }
            req = requests.post(api, data = data)
            print("推送成功，假如没有收到推送，请检查key是否正确")
else:
    print("用户名或者密码错误")
    print(now_time)
