import timeit


def get_mails() -> list:
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5


def for_loop(mails: list, domen: str):
    res = []
    for mail in mails:
        if mail.find(domen) != -1:
            res.append(mail)
    return res


def list_comprehension(mails: list, domen:str):
    return [mail for mail in mails if mail.find(domen) != -1]


def mapper(mails: list, domen:str):
    def map_f(x):
        if x.find(domen) != -1:
            return x
    return map(map_f, mails)


def main():
    n = 9000000
    t_loop = timeit.timeit('for_loop(mails, "gmail.com")',
                           'from __main__ import for_loop, get_mails; mails = get_mails()',
                           number=n)
    t_lc = timeit.timeit('list_comprehension(mails, "gmail.com")',
                         'from __main__ import list_comprehension, get_mails; mails = get_mails()',
                         number=n)
    t_map = timeit.timeit('mapper(mails, "gmail.com")',
                          'from __main__ import mapper, get_mails; mails = get_mails()',
                          number=n)
    res = [t_loop, t_lc, t_map]
    sort_res = list(zip(['loop', 'list comprehension', 'map'], res))
    sort_res.sort(key=lambda x: x[1])
    print(f'it is better to use a {sort_res[0][0]}')
    print(f'{sort_res[0][1]} vs {sort_res[1][1]} vs {sort_res[2][1]}')


if __name__ == '__main__':
    main()