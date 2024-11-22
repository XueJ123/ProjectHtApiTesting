# 导包json
import json

# 使用函数封装
# 适用参数替换静态文件名
class ReadJson(object):

    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        # 打开json文件并获取文件流
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)

if __name__ == '__main__':
    data = (ReadJson("channel.json").read_json())
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expected_result"),
                 data.get("expected_status_code")
                 ))
    print(arrs)