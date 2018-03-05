import tornado.web

# 重点 : 类名不要与文件名重复

class PublicRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        print("触发了了拦截器")

