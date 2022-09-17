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


def find_in_companies(companies: dict, stocks: dict, name: str) -> bool:
    for company, token in companies.items():
        if name.lower() == company.lower():
            print(company, "stock price is", stocks[token])
            return True


def ft_find_key_by_value(companies: dict, value: str) -> str:
    for key, val in companies.items():
        if val == value:
            return key


def find_in_tokens(companies: dict, stocks: dict, tk: str) -> bool:
    tk = tk.upper()
    if tk not in stocks:
        return False
    else:
        company = ft_find_key_by_value(companies, tk)
        print(tk, "is a ticker symbol for", company)
        return True


def get_info(args: list) -> None:
    companies, stocks = companies_n_stocks()
    for name in args:
        if find_in_companies(companies, stocks, name):
            pass
        elif find_in_tokens(companies, stocks, name):
            pass
        else:
            print(name, "is an unknown company or an unknown ticker symbol")


def parse(string: str) -> list:
    ls = string.split(',')
    args = []
    for arg in ls:
        word = ''
        for letter in arg:
            if not letter.isspace():
                word += letter
        if word == '':
            return []
        else:
            args.append(word)
    return args


def main():
    if len(sys.argv) == 2:
        args = parse(sys.argv[1])
        get_info(args)


if __name__ == '__main__':
    main()