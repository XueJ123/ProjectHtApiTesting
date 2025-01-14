# 导包requests
import requests

# 新建文章对象类
class ApiArticle(object):
    # 新建收藏文章方法
    def api_post_collection(self, url, headers, data):
        # 调用post方法并返回响应对象
        return requests.post(url, headers=headers, json=data)

    # 新建取消收藏文章方法
    def api_delete_collection(self, url, headers):
        # 调用delete方法并返回响应对象
        return requests.delete(url, headers=headers)