# Livro com Validação de Limite de Páginas
from time import sleep
from rich import print

class Livro:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.current_page = 1

    def __str__(self):
        return f'{self.title}, {self.pages} páginas.'

    def skip_pages(self, skips, reverse=False):
        step = 1 if not reverse else -1

        for _ in range(0, skips):
            next_page = self.current_page + step
            if next_page < 1 or next_page > self.pages:
                break
            print(f'    página {self.current_page} ...')
            sleep(0.25)
            self.current_page += step

        return f'página {self.current_page} [green]<-- posição atual.[/]'


my_book = Livro('Ventos da Tempestade RPG', 15)
print(my_book.skip_pages(5))
print(my_book.skip_pages(20))
print(my_book.skip_pages(7, reverse=True))
print(my_book.skip_pages(10, reverse=True))
