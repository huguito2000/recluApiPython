import requests
import json

from objetos.obj_clientes import newClient, eliminarCliente
from test.login import loginValido

#se hace login y se optiene el token
respuesta, token, resultado = loginValido()
print('el token es:' + token)
headers = {
    'Authorization': f'Bearer {token}'
}

#se crea un nuevo cliente y se obtiene el clientId
clientId = newClient(headers)

#se elimina el nuevo cliente creado

eliminarCliente(clientId, headers)

