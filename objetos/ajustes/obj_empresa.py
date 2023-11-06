import os

from objetos.funciones import base, foto, subirArchivo, sendPatch

url = 'https://pre.micros.involverh.com.mx/user/company'
myBody = [
    {
        "op": "replace",
        "path": "/businessName",
        "value": "involver"
    },
    {
        "op": "replace",
        "path": "/companySize",
        "value": "DE51A250"
    },
    {
        "op": "replace",
        "path": "/industry",
        "value": {
            "industryId": "40288088798a3b0501798a58c8c90058",
            "englishName": " Internet services",
            "spanishName": "Servicios de Internet",
            "keySystem": "MEX"
        }
    },
    {
        "op": "replace",
        "path": "/sector",
        "value": {
            "sectorId": "4028808879868679017986ac3c45000a",
            "englishName": "Technology and telecommunications",
            "spanishName": "Tecnología y telecomunicaciones",
            "keySystem": "MEX"
        }
    },
    {
        "op": "replace",
        "path": "/typeCompany",
        "value": {
            "catalogSystemId": "2c9f906e8684a58a0186942003290004",
            "name": "Nacional",
            "type": "typeCompany",
            "status": True,
            "keySystem": "MEX"
        }
    },
    {
        "op": "replace",
        "path": "/country",
        "value": "MX"
    }
]

def empresa(headers):
    sendPatch(url, headers, myBody, 200)

