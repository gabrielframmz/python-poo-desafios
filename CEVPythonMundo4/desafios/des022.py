# Controle Remoto em Python
from rich import print
from rich.panel import Panel


class TV:
    def __init__(self, polegadas, ligada = False, canal = 1, volume = 2):
        self.polegadas = polegadas
        self.ligada = ligada
        self.canal = canal
        self.canal_max = 5
        self.volume = volume
        self.volume_max = 10

    def __str__(self):
        return f'\nEsta é a sua TV. Está {"LIGADA" if self.ligada else "DESLIGADA"}, no Canal {self.canal} e Volume {self.volume}.'

    def controle(self):
        while True:
            if not self.ligada:
                renderable = '[red]A TV está desligada.[/]'
            else:
                renderable = '[white on blue]' + ('~' * (self.polegadas - 4)) + '[/]'
                renderable += f'\nCANAL '
                for canal in range(1, self.canal_max + 1):
                    renderable += f'[yellow on yellow][{canal}][/]' if self.canal == canal else f'[{canal}]'
                renderable += f'\nVOLUME [ {self.volume} ] ' + '[white on purple]' + (' ' * self.volume) + '[/]'
            print(Panel(
                renderable,
                title='[ :tv: ]' if self.ligada else '[ ! TV :stop_sign: ]',
                width=self.polegadas
            ))

            option = str(input('\n< CH > | - VOL + | -->  '))
            if option == '@':
                self.ligada = not self.ligada
            elif option in ['<', '>'] and self.ligada:
                self.mudar_canal(option)
            elif option in ['-', '+'] and self.ligada:
                self.mudar_volume(option)
            else:
                print(self.__str__())

    def mudar_canal(self, button):
        if button == '<' and self.canal != 1:
            self.canal -= 1
        elif button == '>' and self.canal != self.canal_max:
            self.canal += 1

    def mudar_volume(self, button):
        if button == '-' and self.volume != 0:
            self.volume -= 1
        elif button == '+' and self.volume != self.volume_max:
            self.volume += 1


samsung_oled_4k_cinema_premium = TV(32, True)
samsung_oled_4k_cinema_premium.controle()
