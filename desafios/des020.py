# Gamer Class
from rich import print as rprint
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def __str__(self):
        return self.nick

    def add_favoritos(self, *games):
        for i in range(len(games)):
            self.favoritos.append(games[i].capitalize())

    def ficha(self):
        renderable = f'[red]NOME REAL: {self.nome}[/]'
        renderable += f'\n[underline]JOGOS FAVORITOS:[/]'

        self.favoritos.sort()
        for game in self.favoritos:
            renderable += f'\n:video_game: {game}'

        return rprint(Panel(renderable, title=f'[green] xxx {self.nick} xxx [/]'))


j1 = Gamer('Jão', 'Shaolin Pigkiller')
print(j1)
j1.add_favoritos('minecraft', 'free fire', 'god of war - ps2')
j1.ficha()
