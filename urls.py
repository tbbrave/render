# coding:utf-8
import tornado.web
from handler.index import indexHandler, userIndexHandler
from handler.login import signupHandler, loginHandler
from handler.error import errorHandler
from handler.request import Request

urls = [
    (r'.*',Request),
    (r'/', indexHandler),  # 首页/查看全部作品
    (r'/login', loginHandler),  # 登陆界面
    (r'/signup', signupHandler),  # 申请新用户界面
    (r'/user', userIndexHandler),  # 用户界面首页
    # 处理错误
    (r'/error/(.*)/(.*)', errorHandler),  # 各类报错信息
    (r'/error/404', errorHandler),
    (r'/error/', errorHandler),
]
