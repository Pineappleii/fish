import base64
import datetime
import hashlib
import hmac
import time


def byte_secret(secret):
    missing_padding = len(secret) % 8
    if missing_padding != 0:
        secret += '=' * (8 - missing_padding)
    return base64.b32decode(secret, casefold=True)


def int_to_bytestring(i, padding=8):
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(bytearray(reversed(result)).rjust(padding, b'\0'))


def generate_otp(secret):
    """
    生成MFA安全码
    :param secret: 用户秘钥
    :return: MFA安全码
    """
    for_time = datetime.datetime.now()
    i = time.mktime(for_time.timetuple())
    simulate_input = int(i / 30)
    digest = hashlib.sha1
    digits = 6
    if simulate_input < 0:
        raise ValueError('input must be positive integer')
    hasher = hmac.new(byte_secret(secret), int_to_bytestring(simulate_input), digest)
    hmac_hash = bytearray(hasher.digest())
    offset = hmac_hash[-1] & 0xf
    code = ((hmac_hash[offset] & 0x7f) << 24 |
            (hmac_hash[offset + 1] & 0xff) << 16 |
            (hmac_hash[offset + 2] & 0xff) << 8 |
            (hmac_hash[offset + 3] & 0xff))
    str_code = str(code % 10 ** digits)
    while len(str_code) < digits:
        str_code = '0' + str_code
    return str_code
