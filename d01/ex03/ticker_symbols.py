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


def ft_find_key_by_value(companies: dict, value: str) -> str:
    for key, val in companies.items():
        if val == value:
            return key


def print_ticket_info(tk):
    companies, stocks = companies_n_stocks()
    tk = tk.upper()
    if tk not in stocks:
        print("Unknown ticket")
    else:
        company = ft_find_key_by_value(companies, tk)
        print(company, stocks[tk])


def main():
    if len(sys.argv) == 2:
        print_ticket_info(sys.argv[1])


if __name__ == '__main__':
    main()