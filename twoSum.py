def test():
    nums = [3, 1, 2, 15, 3]
    target = 6
    d = {}
    for i, item in enumerate(nums):
        c = target - item
        if c in d:
            return [d[c], i]
        d[item] = i


print(test())
