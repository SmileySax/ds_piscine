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


def find_stock_info(name: str):
    companies, stocks = companies_n_stocks()
    for company, token in companies.items():
        if name.lower() == company.lower():
            print(stocks[token])
            return
    print("Unknown company")


def main():
    if len(sys.argv) == 2:
        find_stock_info(sys.argv[1])


if __name__ == '__main__':
    main()