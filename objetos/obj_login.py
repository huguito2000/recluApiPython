from objetos.funciones import base
from objetos.funciones import sendPost

url = base + 'notification/login'
myObj = {"email": "huguito.reclutador@yopmail.com", "password": "Abcd.1234"}


def HacerLogin():
    resultado, headers = sendPost(url, myObj, 200)
    print('se realizo el login')
    return resultado, headers
