import sys


def get_name_from_tab(mail: str, addr: str) -> str:
    with open(addr, 'r') as file:
        lines = file.readlines()
    for line in lines:
        pos = line.find(mail)
        if (pos != -1) and (line[pos + len(mail)] == '\n'):
            return line[:line.find('\t')]
    raise EOFError


def letter(mail: str) -> str:
    try:
        name = get_name_from_tab(mail, 'employees.tsv')
        return f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with " +\
               f"you. That’s a precondition for the professionals that our company hires."
    except EOFError:
        return f"We are sorry not to see {mail} in our base. Check correctness of e-mail"


def main():
    if len(sys.argv) == 2:
        text = letter(sys.argv[1])
        print(text)


if __name__ == '__main__':
    main()