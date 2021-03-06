from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from app import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(5000)             # 监听 5000 端口，flask默认 5000 端口
IOLoop.current().start()
