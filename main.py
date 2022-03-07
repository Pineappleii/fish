import tornado.ioloop
import tornado.web

from _env_settings import settings
import zFrontier_utils
from base import BaseHandler
from bullshit import BullshitGenerator

from log_utils import logger
from mfa_utils import generate_otp


class HealthCheckHandler(BaseHandler):
    async def get(self):
        self.write('hello')


class JmsMFAHandler(BaseHandler):
    async def get(self):
        mfa_code = generate_otp(settings.JMSMFA)
        logger.info(f'MFA验证码:{mfa_code}')
        self.write(f'MFA验证码:{mfa_code}')


class AliMFAHandler(BaseHandler):
    async def get(self):
        mfa_code = generate_otp(settings.ALIMFA)
        logger.info(f'MFA验证码:{mfa_code}')
        self.write(f'MFA验证码:{mfa_code}')


class zFrontierHandler(BaseHandler):
    async def get(self):
        zFrontier = zFrontier_utils.zFrontier()
        res = zFrontier.main()
        logger.info(f'zFrontier返回结果:{res}')
        self.write(res)


class BullshitHandler(BaseHandler):
    async def get(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        c = self.get_argument('c')
        bullshit = BullshitGenerator()
        res = bullshit.main(a, b, c)
        self.write(res)


def make_app():
    return tornado.web.Application([
        (r'/', HealthCheckHandler),
        (r'/jms', JmsMFAHandler),
        (r'/ali', AliMFAHandler),
        (r'/zFrontier', zFrontierHandler),
        (r'/bullshit', BullshitHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
