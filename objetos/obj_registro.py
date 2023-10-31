import requests
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

urlCrearPass = base + 'notification/registry/create-pass?password=Abcd.1234'

urlRecruiter = base + 'user/recruiter'
dataRecruite1 = data = [
	{
    	"op": "replace",
    	"path": "/stepsStatus",
    	"value": 0
	}
]

urlEmailCheck: str = str(base + 'notification/session-aux/check-email?email=' + correo + '&code=')

dataCheckEmail = [
    {
        "op": "replace",
        "path": "/stepsStatus",
        "value": 1
    }
]

nombres = [
    {
        "op": "replace",
        "path": "/user/name",
        "value": "hugo "
    },
    {
        "op": "replace",
        "path": "/user/lastName",
        "value": "rodriguez"
    },
    {
        "op": "replace",
        "path": "/user/secondLastName",
        "value": ""
    },
    {
        "op": "replace",
        "path": "/stepsStatus",
        "value": 8
    }
]

urlCompany = base + 'user/company'
company = [
    {
        "op": "replace",
        "path": "/businessName",
        "value": "involve"
    },
    {
        "op": "replace",
        "path": "/companySize",
        "value": "DE1A10"
    },
    {
        "op": "replace",
        "path": "/country",
        "value": "MX"
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
        "path": "/industry",
        "value": {
            "industryId": "40288088798a3b0501798a58ca500059",
            "englishName": " Software",
            "spanishName": "Software",
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
        "path": "/invoiceNotification",
        "value": True
    }
]