from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

define('port', type=int, default=18000)

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello from tornado')


def main():
    parse_command_line()
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application(
        [('/hello-tornado', HelloHandler),
         ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
         ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
