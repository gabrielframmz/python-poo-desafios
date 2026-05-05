import secrets
import string
from os import makedirs
from pathlib import Path


def generate(length: int = 8) -> str:
    potential = string.ascii_letters + string.digits + '.<>/?^~-_=+*&%$#@!|'
    password = ''.join(secrets.choice(potential) for _ in range(length))
    return password


def store(password: str, tag: str) -> None:
    makedirs(f'./Passwords/', exist_ok=True)
    path = Path('./Passwords/passwords.txt')

    if not path.exists():
        path.write_text(
            'DO NOT SHARE THIS FILE! '
            'IT IS RECOMMENDED TO ONLY USE THIS FILE TEMPORALLY UNTIL YOU SAVE YOUR PASSWORDS SOMEWHERE SAFER.\n'
        )

    with open(path, 'a') as file:
        file.write(f'\n{tag}: {password}')

    full_path = path.resolve()
    print(
        f'  \033[0;33mSenha salva!!!\n'
        f'  Caminho: {full_path}\033[m'
    )

