from random import randint, choice


def generate(length: int = 8) -> str:
    password = ''
    for _ in range(0, length):
        number = str(randint(0, 9))

        char = choice([number])
        password += char
    return password
