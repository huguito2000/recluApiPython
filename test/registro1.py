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

#se manda un PUT con la creacion de la contraseña
sendPut(urlCrearPass, headers, 200)
print('se mando la contraseña')

# se manda un PATCH con el recruiter y la data1
sendPatch(urlRecruiter, headers, dataRecruite1, 200)
print('se mando el recruiter1 del registro')

#paso2 envio de codigo
#se manda el check email
sendPostSinBody(urlEmailCheck + code, 200)
print('se manda el check email')

#se manda recruiter PATCH
sendPatch(urlRecruiter, headers, dataCheckEmail, 200)
print('se mando recruiter check email')

#paso3 formulario
#se manda PATCH del formulario de nombre
sendPatch(urlRecruiter, headers, nombres, 200)
print('se manda formulario nombre')

#se manda PATCH del formulario de compañia
sendPatch(urlCompany, headers, company, 200)
print('se manda la compañia')

