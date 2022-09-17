def data_types():
    i = 5
    s = "string"
    f = 5.05
    b = True
    l = []
    d = {}
    t = (i, s)
    se = set(s)
    all_inst = [i, s, f, b, l, d, t, se]
    res = "["
    for n, inst in enumerate(all_inst):
        res += type(inst).__name__
        if (n < len(all_inst) - 1):
            res += ', '
    res += "]"
    print(res)


if __name__ == '__main__':
    data_types()
