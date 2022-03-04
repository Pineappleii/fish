import os

from dotenv import load_dotenv


class settings:
    load_dotenv(verbose=True)
    JMSMFA = os.getenv('JMSMFA')
    ALIMFA = os.getenv('ALIMFA')
    ZF_USERNAME = os.getenv('ZF_USERNAME')
    ZF_PASSWORD = os.getenv('ZF_PASSWORD')
    ZF_USERID = os.getenv('ZF_USERID')
