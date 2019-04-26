"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
def test():
    x = 123
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        str_len = len(str(x))
        for i in range(0, str_len):
            if i + 1 > str_len // 2:
                return True
            start = x // 10 ** i % 10
            end = x // 10 ** (str_len - 1 - i) % 10
            if start != end:
                return False

    return True


print(test())
