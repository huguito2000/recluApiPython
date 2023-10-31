from test.prueba import post
from objetos.obj_login import url, myObj


resultado, headers = post(url,  myObj, 200)

print('el token es: ' + headers['token'])
