from module import password as pw


def main() -> None:
    print(f'{"_*_" * 5}PASSWORD GENERATOR{"_*_" * 5}')

    while True:
        print('_' * 48)
        try:
            length = int(input('\033[0;34mNúmero de caracteres:\033[m '))
            password = pw.generate(length)
        except ValueError:
            print('\033[0;31mEntrada inválida! Usando tamanho padrão (8)\033[m')
            password = pw.generate()

        save = input(f'\033[0;33m{password}\033[m \nSalvar? (y/n)\n').lower()
        if save == 'y':
            tag = input('\033[0;35mEtiqueta/Nome da senha:\033[m ')
            pw.store(password, tag)

        if input('Fechar programa? (y/n)\n').lower() == 'y':
            break


if __name__ == '__main__':
    main()
