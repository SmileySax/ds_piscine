class Research:

    def file_reader(self):
        with open('../ex00/data.csv', 'r', encoding='utf-8') as data:
            return data.read()


def main():
    research = Research()
    print(research.file_reader())

if __name__ == '__main__':
    main()