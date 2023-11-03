from objetos.funciones import sendPut, sendPatch, sendPostSinBody, sendPost
from datetime import datetime
from objetos.funciones import base
now = datetime.now()
correo = 'reclu' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)
url = base + 'notification/registry'
myBody = {
    "email": correo,
    "userRol": "RECRUITER_ADMIN",
    "keySystem": "MEX",
    "password": "Abcd.1234",
    "phone": "5569777077",
    "acceptPrivacy": True,
    "acceptTerms": True,
    "acceptCookies": True
}

#Paso1
#registry Se mandan los datos de registro y se obtiene el token
def reg1():
    resultado, headers = sendPost(url, myBody, 201)
    print('reg1: se mandaron los datos')
    return resultado, headers



