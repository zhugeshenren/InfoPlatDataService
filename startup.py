import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from Project.urls import urlpattern;
import os.path;

from tornado.options import define, options


define("port", default=8001, help="run on the given port", type=int)


# 先写框架，再优化

if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = tornado.web.Application(  handlers=urlpattern,
                                    static_path=os.path.join(os.path.dirname(__file__), "static"),  # 这里增加设置了静态路径
                                    template_path = os.path.join(os.path.dirname(__file__), "app/Operation"),
                                    debug=True,
                                  )

    # 巧妙地通过 Configurable的 __new__方法构造了对象
    http_server = tornado.httpserver.HTTPServer(app);

    # 开始监听
    http_server.listen(options.port)

    # 开始循环
    tornado.ioloop.IOLoop.instance().start()