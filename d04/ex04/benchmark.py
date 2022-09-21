import timeit
import random
from collections import Counter


def gen_nums() -> list:
    return [random.randint(0, 100) for i in range(1000000)]


def my_func(nums: list) -> dict:
    res = {}
    for num in range(101):
        res[num] = 0
    for num in nums:
        res[num] += 1
    return res


def my_top(nums: list) -> dict:
    all = my_func(nums)
    ls = list(all.items())
    ls.sort(key=lambda x: -x[1])
    return dict(ls[:10])


def ctr_func(nums: list) -> dict:
    return dict(Counter(nums))


def ctr_top(nums: list) -> dict:
    return dict(Counter(nums).most_common(10))


def main():
    nums = gen_nums()
    n = 100
    t_my_f = timeit.timeit('my_func(nums)',
                           'from __main__ import my_func, gen_nums; nums = gen_nums()',
                           number=n)
    t_ctr_f = timeit.timeit('ctr_func(nums)',
                            'from __main__ import ctr_func, gen_nums; nums = gen_nums()',
                            number=n)
    t_my_top = timeit.timeit('my_top(nums)',
                             'from __main__ import my_top, gen_nums; nums = gen_nums()',
                             number=n)
    t_ctr_top = timeit.timeit('ctr_top(nums)',
                              'from __main__ import ctr_top, gen_nums; nums = gen_nums()',
                              number=n)

    print(f'my function: {t_my_f}')
    print(f'Counter: {t_ctr_f}')
    print(f'my top: {t_my_top}')
    print(f'Counter\'s function: {t_ctr_top}')


if __name__ == '__main__':
    main()