import logging

from common_utils import mkdir

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级总开关

log_path = 'logs/'
mkdir(log_path)
logfile = 'logs/fish.log'
formatter = logging.Formatter(
    fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: \n%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

formatter_console = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# log文件的配置
handler = logging.FileHandler(logfile)
handler.setLevel(logging.WARNING)
handler.setFormatter(formatter)

# 控制台的配置
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter_console)

logger.addHandler(handler)
logger.addHandler(console)
