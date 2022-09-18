import sys


def do_caesarcrypt(text: str, shift: int) -> str:
    new = []
    n = ''
    for letter in text:
        if letter.isalpha() and letter != ' ':
            if ord(letter) < ord('a'):
                code = ord('A')
            else:
                code = ord('a')
            code += (26 + ord(letter) - code + shift) % 26
            new.append(chr(code))
        else:
            new.append(letter)
    return "".join(new)


def ft_crypt(params: list) -> str:
    errtext = "input format: caesar.py [encode/decode] string #shift"
    if not params[2].isnumeric():
        return errtext
    if params[0].lower() == 'encode':
        shift = int(params[2])
    elif params[0].lower() == 'decode':
        shift = -int(params[2])
    else:
        return errtext
    if not params[1].isascii():
        return errtext
    return do_caesarcrypt(params[1], shift)


def main():
    if len(sys.argv) == 4:
        text = ft_crypt(sys.argv[1:])
        print(text)
    else:
        print("input format: caesar.py [encode/decode] string #shift")


if __name__ == '__main__':
    main()