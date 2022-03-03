from os import environ


class settings:
    JMSMFA = environ.get('JMSMFA')
    ALIMFA = environ.get('ALIMFA')
    ZF_USERNAME = environ.get('ZFRONTIER_USERNAME')
    ZF_PASSWORD = environ.get('ZFRONTIER_PASSWORD')
    ZF_USERID = environ.get('ZFRONTIER_USERID')
