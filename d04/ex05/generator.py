import sys
import resource


def func(path: str):
    with open(path, 'r') as file:
        line = 'smth'
        while line:
            line = file.readline()
            yield line


def main(path: str):
    lines = func(path)
    for line in lines:
        pass

    resource_usage = resource.getrusage(resource.RUSAGE_SELF)
    mem = resource_usage.ru_maxrss / (1 << 30)
    times = resource_usage.ru_utime + resource_usage.ru_stime
    print(f'Peak Memory Usage = {mem:.3f} GB')
    print(f'User Mode Time + System Mode Time = {times:.2f}s')


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            main(sys.argv[1])
    except FileNotFoundError as err:
        print(err)
