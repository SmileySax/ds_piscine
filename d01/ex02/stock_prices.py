import sys


def companies_n_stocks() -> tuple:
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS


def find_stock_info(name):
    companies, stocks = companies_n_stocks()
    if name not in companies:
        print("Unknown company")
    else:
        print(stocks[companies[name]])


def main():
    if len(sys.argv) == 2:
        find_stock_info(sys.argv[1])


if __name__ == '__main__':
    main()