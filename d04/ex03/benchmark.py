import timeit
import sys
from functools import reduce


def do_loop(n: int):
    summ = 0
    for i in range(1, n):
        summ += i*i
    return summ


def do_reduce(n: int):
    def fn(x, y):
        return x + y * y
    return reduce(fn, range(1, n))


def main(fn: str, n_iter: int, n: int):
    if fn in {'loop', 'reduce'}:
        res = timeit.timeit(f'do_{fn}({n})',
                            f'from __main__ import do_{fn}',
                            number=n_iter)
    else:
        res = 'Expected format: ./benchmark.py {loop/reduce} #n_of_iterations, #n_for_sum'
    print(res)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    else:
        print('Expected format: ./benchmark.py {loop/reduce} #n_of_iterations #n_for_sum')