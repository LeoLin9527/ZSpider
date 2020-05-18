"""
@file:youdao.py
@time:2019/7/16-11:02
"""
import json
import requests
from translate.youdaoEncrypte import get_md5, get_ts_salt, get_sign


class YouDao:
    def __init__(self, key, ):
        self.key = key  # 翻译关键字
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.UA = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        self.headers = {
            "User-Agent": self.UA,
            "Referer": "http://fanyi.youdao.com/",
        }
        myappVersion = self.UA
        # 四个加密参数
        self.bv, self.ts, self.salt, self.sign = self.generateSaltSign(myappVersion)

    def generateSaltSign(self, myappVersion):
        # navigator.appVersion 的 md5 加密
        bv = get_md5(myappVersion)
        ts, salt = get_ts_salt()
        sign = get_sign(self.key, salt)

        return bv, ts, salt, sign

    def run(self):
        """headers里面有一些参数是必须的"""
        data = {
            'i': self.key,  # 需要翻译的单词
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            "salt": self.salt,
            "sign": self.sign,
            "ts": self.ts,
            "bv": self.bv,
            "doctype": "json",
            "version": 2.1,
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
        }

        session = requests.session()
        # 用于获取后台设置的cookie，若无Cookie{"errorCode":50}
        session.get(self.headers["Referer"])

        resp = session.post(self.url, data=data, headers=self.headers)
        info_dict = json.loads(resp.text)

        if 'translateResult' in info_dict:
            try:
                result = info_dict['translateResult'][0][0]['tgt']
                print("有道翻译 :", result)
                return result
            except:
                print("something error")
        else:
            print("something failed:", resp.text)


if __name__ == '__main__':
    key = input("需要翻译的单词:")
    y = YouDao(key)
    y.run()
