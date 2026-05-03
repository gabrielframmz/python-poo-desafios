import secrets
import string
from os import makedirs


def generate(length: int = 8) -> str:
    potential = string.ascii_letters + string.digits + '.<>/?^~-_=+*&%$#@!|'
    password = ''
    for _ in range(0, length):
        char = secrets.choice(potential)
        password += char
    return password


def store(password: str, tag: str) -> None:
    makedirs(f'./Passwords/', exist_ok=True)
    path = f'./Passwords/passwords.txt'

    try:
        open(path, 'r')
    except FileNotFoundError:
        f = open(path, 'w')
        f.write('DO NOT SHARE THIS FILE! '
                'IT IS RECOMMENDED TO ONLY USE THIS FILE TEMPORALLY UNTIL YOU SAVE YOUR PASSWORDS SOMEWHERE SAFER.'
                '\n')
        f.close()
    finally:
        f = open(path, 'a')
        f.write(f'\n{tag}: {password}')
        f.close()

    print('\033[0;33mSenha salva!!!\033[m')
