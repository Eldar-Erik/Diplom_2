import random

def random_reg_username():
    return f'dikopp{random.randint(100, 999)}'

def random_reg_email():
    log = random_reg_username()
    return f'{log}@yasha.ru'

def random_reg_pass():
    return f'{random.randint(100000, 999999)}'

def order_data():
    ingridients = {
                "ingredients": ["61c0c5a71d1f82001bdaaa70"]
                }
    return ingridients

def order_data_empty():
    ingridients = {
                "ingredients": []
                }
    return ingridients

def order_data_false():
    ingridients = {
                "ingredients": ["3"]
                }
    return ingridients