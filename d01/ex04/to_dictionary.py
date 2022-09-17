def inputs() -> list:
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples


def main():
    inputs_list = inputs()
    d = {}
    for country, number in inputs_list:
        if number not in d:
            d[number] = []
        d[number].append(country)

    for key, value in d.items():
        for attr in value:
            print(f"'{key}' : '{attr}'")


if __name__ == '__main__':
    main()