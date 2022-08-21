import os
from user import User
from items import Item
import mysql.connector

def cls():
    os.system('cls')

login = input("login: ")
password = input("podaj hasło: ")
cls()
user = User(login,password)
# user.login_to_app()
user.create_account()
