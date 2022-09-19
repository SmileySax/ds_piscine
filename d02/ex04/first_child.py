import random
import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def __check__(self, has_header):
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

    def file_reader(self, has_header=True) -> list:
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
        def __init__(self, data: list):
            self.data = data

        def counts(self) -> tuple:
            tails = 0
            heads = 0
            for line in self.data:
                heads += line[0]
                tails += line[1]
            return heads, tails

        def fractions(self, heads: int, tails: int) -> tuple:
            total = heads + tails
            return heads/total*100, tails/total*100

    class Analytics(Calculations):
        def predict_random(self, n: int) -> list:
            preds = []
            for i in range(n):
                pred = random.randint(0, 1)
                preds.append([pred, 1 - pred])
            return preds

        def predict_last(self):
            return self.data[-1]


def main():
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        try:
            res = research.file_reader()
            print(res)
        except Exception as error:
            print("There is an error:", error)
            return
        analytics = research.Analytics(res)
        sums = analytics.counts()
        print(*sums)
        percents = analytics.fractions(*sums)
        print(*percents)
        rnds = analytics.predict_random(3)
        print(rnds)
        last = analytics.predict_last()
        print(last)


if __name__ == '__main__':
    main()