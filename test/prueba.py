import requests
from objetos.funciones import sendPut, sendPatch, sendPostSinBody, sendPost
from objetos.obj_registro import url, myBody, dataCheckEmail, dataRecruite1, nombres, company, urlCrearPass, urlEmailCheck, urlRecruiter, urlCompany
#Paso1
#registry Se mandan los datos de registro y se obtiene el token
resultado, headers = sendPost(url, myBody, 201)
code = str(resultado['user']['checkCode'])
print('el codigo es: ' + code)
print('los headers son: ' + str(headers))
token = headers['token']
token = str(token.replace('Bearer ', ''))
print('el token es:' + token)
headers = {
    'Authorization': f'Bearer {token}'
}
