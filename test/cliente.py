import requests
from objetos.funciones import sendPostHeaders
from objetos.obj_clientes import urlCliente, cliente
from test.login import login

head, token = login()
print('el token es:' + token)
headers = {
    'Authorization': f'Bearer {token}'
}
sendPostHeaders(urlCliente, headers, cliente, 200)


