from app.Extension.PublicClass import PublicRequestHandler

from app.Extension.PublicClass import PublicRequestHandler
import json
from urllib.parse import unquote
import os
from tornado.escape import json_decode
import re
from app.Extension.DecodeData import decodeHtmlBody
from tornado.web import authenticated


# 响应添加图片请求 通过设置headers让其支持跨域
# #必须优化
class AddImgControllers(PublicRequestHandler):

    def get(self, *args, **kwargs):
        self.finish('zhuge');

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

    # 允许http 跨域
    def set_default_headers(self):
        print("setting headers")
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名，进行限制
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # 返回json 用于回显
    def post(self, *args, **kwargs):
        upload_path = 'C:/files'  # 文件的暂存路径
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        print(upload_path)
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])

        tmp = {"status": 1,"url": ""};
        # 返回地址
        tmp['url'] = 'http://47.94.128.163:8000/static/files/'+filename;
        self.write(json.dumps(tmp));