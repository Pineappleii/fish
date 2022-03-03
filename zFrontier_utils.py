import requests

from bs4 import BeautifulSoup

from _env_settings import settings


class zFrontier:

    def __init__(self):
        self.zFrontier = requests.session()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/80.0.3987.163 Safari/537.36 '
        self.headers = {
            'Referer': 'https://www.zfrontier.com/',
            'User-Agent': self.user_agent,
        }

    def zFrontierLogin(self, account, password):
        postUrl = 'https://www.zfrontier.com/api/login/mobile'
        postData = {
            'mobile': account,
            'password': password,
        }
        self.zFrontier.post(postUrl, data=postData, headers=self.headers)

    def signIn(self):
        self.zFrontierLogin(settings.ZF_USERNAME, settings.ZF_PASSWORD)
        self.zFrontier.get(f'https://www.zfrontier.com/user/home/{settings.ZF_USERID}',
                           headers=self.headers, allow_redirects=False)
        checkInUrl = 'https://www.zfrontier.com/api/checkIn'
        response = self.zFrontier.post(checkInUrl, headers=self.headers, allow_redirects=False)
        return response.text

    def main(self):
        response = self.signIn()
        soup = BeautifulSoup(response, features='html.parser')
        [s.extract() for s in soup('svg')]
        [s.extract() for s in soup('a')]
        return soup.get_text()


if __name__ == '__main__':
    zf = zFrontier()
    res = zf.main()
    print(res)
