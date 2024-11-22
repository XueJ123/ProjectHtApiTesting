# 导包unittest ApiChannels
import unittest
from api.api_channels import ApiChannels
from parameterized import parameterized
from tools.read_json import ReadJson


def get_data():
    data = ReadJson("channel.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expected_result"),
                 data.get("expected_status_code")
                 ))
    return arrs

# 新建测试类
class TestChannels(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self, url, headers, expected_result, expected_status_code):
        # 临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # 提示：token在登录成功后返回，并且在token前面有Bearer和空格
        # headers = {"Content-Type": "application/json",
        #            "Authorization": "Bearer 登录成功后返回的token值"
        #            }
        # 调用获取用户频道列表方法
        r = ApiChannels().api_get_channels(url, headers)
        # 调试信息 打印响应结果
        print(r.json())
        # 断言 状态码
        self.assertEquals(expected_status_code, r.status_code)
        # 断言 响应信息
        self.assertEquals(expected_result, r.json()['message'])