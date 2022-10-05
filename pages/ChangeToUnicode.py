def turn_to_unicode(string):
    res = ''
    for v in string:
        res = res + hex(ord(v)).upper().replace('0X', '\\u')
    print(string, '的Unicode编码为', res)
    return res


if __name__ == '__main__':
    turn_to_unicode('自动驾驶开关')
