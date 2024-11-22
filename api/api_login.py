# 导入 request
import json

import requests


# 新建类 登录接口对象
class ApiLogin(object):
    # 新建方法 登录方法
    def api_post_login(self, url, mobile, code):
        # headers定义
        headers = {"Content-Type": "application/json"}
        # data定义
        data = {"mobile": mobile, "code": code}
        #调用post并返回响应对象
        return requests.post(url, headers=headers, json=data)
