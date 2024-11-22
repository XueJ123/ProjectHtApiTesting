# 导包unittest ApiArticle
import unittest
from api.api_article import ApiArticle
from parameterized import parameterized
from tools.read_json import ReadJson


def get_data_add():
    data = ReadJson("article_add.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expected_result"),
                 data.get("expected_status_code")
                 ))
    return arrs

def get_data_cancel():
    data = ReadJson("article_cancel.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expected_status_code")
                 ))
    return arrs

# 新建测试类 继承
class TestArticle(unittest.TestCase):
    # 新建收藏文章方法
    @parameterized.expand(get_data_add())
    def test01_collection(self, url, headers, data, expected_result, expected_status_code):
        # 临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        # headers = {"Content-Type": "application/json",
        #           "Authorization": "Bearer 登录成功后返回的token值"
        #           }
        # data = {"target": 1}
        # 调用收藏文章方法
        r = ApiArticle().api_post_collection(url, headers, data)
        # 调试查看响应数据测试结果
        print("收藏响应数据为： ", r.json())
        # 断言响应状态码
        self.assertEquals(expected_status_code, r.status_code)
        # 断言响应信息
        self.assertEquals(expected_result, r.json()['message'])

    # 新建取消收藏文章方法
    @parameterized.expand(get_data_cancel())
    def test02_cancel(self, url, headers, expected_status_code):
        # 临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # headers = {"Content-Type": "application/x-www-form-urlencoded",
        #            "Authorization": "Bearer 登录成功后返回的token值"
        #            }
        # 调用取消收藏方法
        r = ApiArticle().api_delete_collection(url, headers)
        # 断言状态码
        self.assertEquals(expected_status_code, r.status_code)