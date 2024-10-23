import random

def random_reg_username():
    return f'dikopp{random.randint(100, 999)}'

def random_reg_email():
    log = random_reg_username()
    return f'{log}@yasha.ru'

def random_reg_pass():
    return f'{random.randint(100000, 999999)}'