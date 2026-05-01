from module import password as pw


def main() -> None:
    print(f'{"_*_" * 5}PASSWORD GENERATOR{"_*_" * 5}')

    try:
        length = int(input('Número de caracteres: '))
    except ValueError:
        length = 8

    password = pw.generate(length)
    print(password)


if __name__ == '__main__':
    main()
