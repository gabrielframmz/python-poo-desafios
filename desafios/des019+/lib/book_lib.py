# Versão expandida do desafio 19;
# simula a abertura das páginas e seu conteúdo.
# Extremamente básico e experimental.

from rich import print
from time import sleep
from os import makedirs


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

    def open_current_page(self):
        makedirs(f'./books/{self.title.upper()}/', exist_ok=True)
        page_path = f'./books/{self.title.upper()}/{self.current_page}.txt'

        try:
            pg = open(page_path, 'r')
            pg.close()
        except FileNotFoundError:
            pg = open(page_path, 'w')
            pg.write(
                f'\nEsta é a página {self.current_page}, parábens por chegar aqui!'
                f'\n'
                f'\nLorem ipsum dolor sit amet consectetur adipiscing elit.'
                f'\nQuisque faucibus ex sapien vitae pellentesque sem placerat.'
                f'\nIn id cursus mi pretium tellus duis convallis.'
                f'\nTempus leo eu aenean sed diam urna tempor.'
                f'\nPulvinar vivamus fringilla lacus nec metus bibendum egestas.'
                f'\nIaculis massa nisl malesuada lacinia integer nunc posuere.'
                f'\nUt hendrerit semper vel class aptent taciti sociosqu.'
                f'\nAd litora torquent per conubia nostra inceptos himenaeos.'
            )
            pg.close()
            self.open_current_page()
        else:
            pg = open(page_path, 'r')
            for txt in pg:
                print(f'{txt}\n')
            pg.close()

