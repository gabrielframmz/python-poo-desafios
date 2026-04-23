# Versão expandida do desafio 19;
# simula a abertura das páginas e seu conteúdo.
# Extremamente básico e experimental.
from module import class_book as cb

def main() -> None:
    book_name = str(input('Dê um nome ao seu livro: '))
    book_pages = int(input('Quantas páginas será possível abrir? '))
    my_book = cb.Livro(book_name, book_pages)

    while True:
        print(
            f'''
                Página atual: {my_book.current_page}
                Ações...
            '''
        )
        op = int(input(
            '''
                1- Abrir página atual.
                2- Pular páginas.
                3- Voltar páginas.
            '''
        ))

        match op:
            case 1:
                my_book.open_current_page()
            case 2:
                np = int(input('PULAR quantas? '))
                my_book.skip_pages(np)
            case 3:
                np = int(input('VOLTAR quantas? '))
                my_book.skip_pages(np, reverse=True)
            case _:
                print('Inválido.')
                break

if __name__ == '__main__':
    main()
