import requests

from _env_settings import settings
from log_utils import logger


class zFrontier:

    def __init__(self):
        """
        实例化类时创建一个session
        """
        self.zFrontier = requests.session()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/80.0.3987.163 Safari/537.36 '
        self.headers = {
            'Referer': 'https://www.zfrontier.com/app/',
            'User-Agent': self.user_agent,
        }

    def zFrontierLogin(self, account, password):
        """
        装备前线登录
        :param account: 手机号
        :param password: 密码
        """
        postUrl = 'https://www.zfrontier.com/api/login/mobile'
        postData = {
            'mobile': account,
            'password': password,
        }
        login_res = self.zFrontier.post(postUrl, data=postData, headers=self.headers)
        logger.info(f'zFrontier登录结果:{login_res.json().get("msg")}')

    def signIn(self):
        """
        装备前线签到
        :return: 签到接口返回值
        """
        self.zFrontierLogin(settings.ZF_USERNAME, settings.ZF_PASSWORD)
        self.zFrontier.get(f'https://www.zfrontier.com/user/home/{settings.ZF_USERID}',
                           headers=self.headers, allow_redirects=False)
        checkInUrl = 'https://www.zfrontier.com/v2/sign'
        response = self.zFrontier.post(checkInUrl, headers=self.headers, allow_redirects=False)
        return response.json()

    def main(self):
        response = self.signIn()
        data = response.get('data')
        level = data.get('bbs_lv')
        score = data.get('bbs_score')
        sign_info = data.get('sign_info').get('desc')
        return f'签到成功(\\*`^`*/) 等级:{level} 积分:{score} {sign_info}'


if __name__ == '__main__':
    zf = zFrontier()
    res = zf.main()
    print(res)
