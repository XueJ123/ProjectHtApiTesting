# 导包 unittest, ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

# 读取数据函数
def get_data():
    datas = (ReadJson("login_more.json").read_json())
    # 新建空列表，添加读取json数据
    arrs = []
    # 使用遍历获取所有的values
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expected_result"),
                     data.get("expected_status_code")
                     ))
    return arrs

# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, mobile, code, expected_result, expected_status_code):
        # 调用登录方法
        s = ApiLogin().api_post_login(url, mobile, code)

        # 调试使用
        print("查看响应结果： ", s.json())
        # 断言响应信息
        self.assertEquals(expected_result, s.json()['message'])
        # 断言状态码
        self.assertEquals(expected_status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
