import requests
import json

from objetos.obj_clientes import newClient, eliminarCliente
from test.login1 import login

#se hace login y se optiene el token
headers, recruiterID = login()

#se crea un nuevo cliente y se obtiene el clientId
clientId = newClient(headers)

#se elimina el nuevo cliente creado
eliminarCliente(clientId, headers)

