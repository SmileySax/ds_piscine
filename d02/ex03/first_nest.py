import sys
import os


class Research:

    def __init__(self, path):
        self.path = path

    def __check__(self, has_header):
        if not os.access(self.path, os.R_OK):
            raise OSError("Read file error")
        with open(self.path, 'r', encoding='utf-8') as data:
            ls = data.readlines()
            k = 1
            if has_header:
                if len(ls[0].split(',')) != 2:
                    raise ValueError('Header is wrongly formatted')
            else:
                k = 0
            if len(ls[k:]) < 1:
                raise ValueError('Empty table')
            for line in ls[1:]:
                digs = list(map(int, line.split(',')))
                if len(digs) != 2 or\
                   digs[0] == digs[1] or\
                   digs[0] not in {0, 1} or\
                   digs[1] not in {0, 1}:
                    raise ValueError('One or more lines are wrongly formatted')

    def file_reader(self, has_header=True):
        self.__check__(self.path)
        with open(self.path, 'r', encoding='utf-8') as data:
            ls = data.readlines()
            if has_header:
                k = 1
            else:
                k = 0
            ls = [list(map(int, line.split(','))) for line in ls[k:]]
            return ls

    class Calculations:

        def counts(self, ls: list) -> tuple:
            tails = 0
            heads = 0
            for line in ls:
                heads += line[0]
                tails += line[1]
            return heads, tails

        def fractions(self, heads: int, tails: int) -> tuple:
            total = heads + tails
            return heads/total*100, tails/total*100


def main():
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        try:
            res = research.file_reader()
            print(res)
        except Exception as error:
            print("There is an error:", error)
            return
        calculations = research.Calculations()
        sums = calculations.counts(res)
        print(*sums)
        percents = calculations.fractions(*sums)
        print(*percents)


if __name__ == '__main__':
    main()