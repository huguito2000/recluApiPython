from objetos.obj_clientes import newClient, eliminarCliente
from test.login1 import login

def cliente():
    try:
        # se hace login y se optiene el token
        respuesta, headers, recruiterID = login()

        # se crea un nuevo cliente y se obtiene el clientId
        clientId = newClient(headers)

        # se elimina el nuevo cliente creado
        eliminarCliente(clientId, headers)
        print('Paso el cliente')
        return 'se hizo la peticion de cliente correctamente'
    except Exception as e:
        print('No paso el cliente', str(e))
        return 'No paso el cliente'



