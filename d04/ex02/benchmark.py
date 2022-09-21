import timeit
import sys


def get_mails() -> list:
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5


def do_loop(mails: list, domen: str):
    res = []
    for mail in mails:
        if mail.find(domen) != -1:
            res.append(mail)
    return res


def do_list_comprehension(mails: list, domen:str):
    return [mail for mail in mails if mail.find(domen) != -1]


def do_map(mails: list, domen:str):
    def map_f(x):
        if x.find(domen) != -1:
            return x
    return map(map_f, mails)


def do_filter(mails: list, domen:str):
    def filt_f(x):
        return x.find(domen) != -1
    return filter(filt_f, mails)


def main(fn: str, n: int):
    if fn in {'loop', 'list_comprehension', 'map', 'filter'}:
        res = timeit.timeit(f'do_{fn}(mails, "gmail.com")',
                            f'from __main__ import do_{fn}, get_mails; mails = get_mails()',
                            number=n)
    else:
        res = 'Expected format: ./benchmark.py {loop/list_comprehension/map/filter} #n_of_iterations'
    print(res)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print('Expected format: ./benchmark.py {loop/list_comprehension/map/filter} #n_of_iterations')