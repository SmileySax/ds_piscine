import sys


def create_tab(addr: str) -> None:
    with open(addr, 'r') as file:
        mails = file.readlines()
    names = [mail[:mail.find('.')].capitalize() for mail in mails]
    surnames = [mail[mail.find('.') + 1:mail.find('@')].capitalize() for mail in mails]
    with open("employees.tsv", 'w') as out:
        out.writelines(f"Name\tSurname\tE-mail\n")
        for name, surname, mail in zip(names, surnames, mails):
            out.writelines(f"{name}\t{surname}\t{mail}")


def main():
    if len(sys.argv) == 2:
        create_tab(sys.argv[1])


if __name__ == '__main__':
    main()