from objetos.funciones import base, sendPostHeaders, sendDelete
from test.login import loginValido

urlCliente = base + 'user/client'

cliente = {
    "name": "involver",
    "sectorId": "4028808879868679017986ac3c45000a",
    "industryId": "40288088798a3b0501798a58ca500059",
    "typeCompany": {
        "catalogSystemId": "2c9f906e8684a58a0186942003290004",
        "name": "Nacional",
        "type": "typeCompany",
        "status": True,
        "keySystem": "MEX"
    },
    "employees": "DE51A250"
}


def newClient(headers):
    client = sendPostHeaders(urlCliente, headers, cliente, 200)
    clientId = client['clientId']
    print('se creo el cliente ' + clientId)
    return clientId


def eliminarCliente(clientId, headers):
    myBody: list = [clientId]
    sendDelete(urlCliente, headers, myBody, 200)
    print('se elimino el cliente')
