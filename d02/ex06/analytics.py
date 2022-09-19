from random import randint
import logging
import requests
import config


class Research:

    logging.basicConfig(filename='analytics.log',
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger()

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
        self.logger.debug('Filereader is reading file')
        self.__check__(self.path)
        with open(self.path, 'r', encoding='utf-8') as data:
            ls = data.readlines()
            if has_header:
                k = 1
            else:
                k = 0
            ls = [list(map(int, line.split(','))) for line in ls[k:]]
            return ls

    def sent_notification(self, result: bool) -> None:
        self.logger.debug('Research is sending notification')
        with open(config.BOT_INFO_PATH, 'r') as file:
            info = file.read()
        bot_token, bot_chatID = info.split()
        if result:
            bot_message = 'Report was created'
        else:
            bot_message = "Report wasn't created"
        message = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        requests.get(message)

    class Calculations:
        def __init__(self, data: list):
            self.data = data

        def counts(self) -> tuple:
            Research.logger.debug('Counter is calculating heads and tails')
            tails = 0
            heads = 0
            for line in self.data:
                heads += line[0]
                tails += line[1]
            return heads, tails

        def fractions(self, heads: int, tails: int) -> tuple:
            Research.logger.debug('Fraction counter is calculating results fractions')
            total = heads + tails
            return heads/total*100, tails/total*100

    class Analytics(Calculations):
        def predict_random(self, n: int) -> list:
            Research.logger.debug('Random predictor is calculating future results')
            preds = []
            for i in range(n):
                pred = randint(0, 1)
                preds.append([pred, 1 - pred])
            return preds

        def predict_last(self):
            Research.logger.debug('Looking for the last result')
            return self.data[-1]

        def save_file(self, data, name, ext):
            Research.logger.debug(f'Saver is saving new file {name}.{ext}')
            with open(name + '.' + ext, 'w') as file:
                file.write(data)

        def counts_given(self, data) -> tuple:
            Research.logger.debug('Analytics calculator is calculating heads and tails in given experement')
            tails = 0
            heads = 0
            for line in data:
                heads += line[0]
                tails += line[1]
            return heads, tails
