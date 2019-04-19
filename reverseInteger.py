def test():
    x = str(-123)
    l = len(x)
    num = ""
    for i in x:
        num += x[l - 1:l]
        l -= 1

    if "-" in num[-1:]:
        num = '-' + num[0:-1]
        
    if -2 ** 31 < int(num) < 2 ** 31 - 1:
        return int(num)
    else:
        return 0


print(test())
