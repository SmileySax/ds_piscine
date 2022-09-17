def ft_commas_to_tabs(ls) -> list:
    vacancies = []
    for string in ls:
        tmp = string.split(',')
        vac = []
        vac.extend(tmp[:2])
        vac.append(",".join(tmp[2:-3]))
        vac.extend(tmp[-3:])
        vacancies.append("\t".join(vac))
    return "".join(vacancies)


def read_n_write():
    with open('ds.csv', 'r', encoding='utf-8') as csv:
        ls = csv.readlines()
    ls = ft_commas_to_tabs(ls)
    with open('ds.tsv', 'w', encoding='utf-8') as tsv:
        tsv.writelines(ls)


if __name__ == '__main__':
    read_n_write()
