from src.helpers import *
from src.data import PAS, LOG_EMAIL, USERNAME

def gen_new_user():
    new_user = {
        "email": random_reg_email(),
        "password": PAS,
        "name": random_reg_username()
    }
    return new_user

def gen_reg_user():
    reg_user = {
        "email": LOG_EMAIL,
        "password": PAS,
        "name": random_reg_username()
    }
    return reg_user

def gen_user_whithout_email():
    brok_user = {
        "email": '',
        "password": PAS,
        "name": random_reg_username()
    }
    return brok_user