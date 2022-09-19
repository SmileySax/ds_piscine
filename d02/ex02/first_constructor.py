import sys
import os


class Research:

    def __init__(self, path):
        self.path = path

    def __check__(self):
        if not os.access(self.path, os.R_OK):
            raise OSError("Read file error")
        with open(self.path, 'r', encoding='utf-8') as data:
            ls = data.readlines()
            if len(ls[0].split(',')) != 2:
                raise ValueError('Header is wrongly formatted')
            if len(ls[1:]) < 1:
                raise ValueError('Empty table')
            for line in ls[1:]:
                digs = list(map(int, line.split(',')))
                if len(digs) != 2 or\
                   digs[0] == digs[1] or\
                   digs[0] not in {0, 1} or\
                   digs[1] not in {0, 1}:
                    raise ValueError('One or more lines are wrongly formatted')

    def file_reader(self):
        self.__check__()
        with open(self.path, 'r', encoding='utf-8') as data:
            return data.read()


def main():
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        try:
            res = research.file_reader()
            print(res)
        except Exception as error:
            print("There is an error:", error)



if __name__ == '__main__':
    main()