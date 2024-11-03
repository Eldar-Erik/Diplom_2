from src.helpers import *
from src.data import PAS, LOG_EMAIL, REG_PASSWORD

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

def log_user():
    login_exist_user = {
        "email": LOG_EMAIL,
        "password": PAS
        }
    return login_exist_user

def false_user():
    login_unexist_user = {
        "email": random_reg_email(),
        "password": REG_PASSWORD
        }
    return login_unexist_user

def update_user():
    update_user_data = {
        "email": random_reg_email(),
        "name": random_reg_username()
        }
    return update_user_data
