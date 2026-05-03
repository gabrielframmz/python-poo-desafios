from module import password as pw


def main() -> None:
    print(f'{"_*_" * 5}PASSWORD GENERATOR{"_*_" * 5}')

    while True:
        try:
            print('_' * 48)
            length = int(input('\033[0;34mNúmero de caracteres:\033[m '))
        except ValueError:
            password = pw.generate()
        else:
            password = pw.generate(length)

        save = input(f'\033[0;33m{password}\033[m \nSalvar? (y/n)\n').lower()
        match save:
            case 'y':
                tag = input('\033[0;35mEtiqueta/Nome da senha:\033[m ')
                pw.store(password, tag)
            case _:
                pass

        end = input(f'Fechar programa? (y/n)\n').lower()
        match end:
            case 'y':
                break
            case _:
                pass


if __name__ == '__main__':
    main()
