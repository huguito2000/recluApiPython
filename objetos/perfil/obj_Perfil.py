from objetos.funciones import base, nombres, apellidos, sendPutBody

urlPerfil = str(base + 'user/recruiter')

nombre = nombres()
apellidoP = apellidos()
apellidoM = apellidos()
body = {
    "recruiterId": "ff8080818ab932ae018abee4d1ea0037",
    "status": "PENDIENTE",
    "showModalPause": False,
    "vacantsActived": -16,
    "nextDailyReport": None,
    "lastDailyReport": None,
    "stepsStatus": 8,
    "positionCompany": "Reclutador",
    "crmLeadId": 32268,
    "vacantsTotal": None,
    "user": {
        "userId": "ff8080818ab932ae018abee4d1ea0038",
        "name": nombre,
        "lastName": apellidoP,
        "checkCode": "2280",
        "secondLastName": apellidoM,
        "email": "huguito.reclutador@yopmail.com",
        "emailVerify": "2023-09-26 16:55:11",
        "phoneVerify": None,
        "password": "$2a$10$9wAYcqxkO4yErmGB7RyGgujJvsuzCGeQIm4VSNtaC8L1pXjX8dBBu",
        "gender": None,
        "photo": "https://s3.us-east-1.amazonaws.com/involve-resources-dev-pre/RECRUITER/ff8080818ab932ae018abee4d1ea0037/URL_PHOTO_jpeg?1698792585223?1698792623512?1698792644109?1699030931707?1699030965694?1699031370628?1699031380563?1699031831714?1699034859707",
        "phone": "+525569777077",
        "attempts": 0,
        "userRol": "RECRUITER_ADMIN",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "acceptNewsletter": False,
        "acceptCookies": True,
        "createDate": "2023-09-22 15:56:22",
        "lastActivity": "2023-11-03 11:17:08",
        "stripeCustomerId": "cus_OgeeGe8OGKpXVz",
        "keySystem": "MEX",
        "urlRegister": None,
        "historyDevices": [],
        "notifications": []
    },
    "company": {
        "companyId": "ff8080818ab932ae018abee4d1e10036",
        "company": None,
        "businessName": "involve",
        "rfc": None,
        "pathLogo": "https://s3.us-east-1.amazonaws.com/involve-resources-dev-pre/COMPANY/ff8080818ab932ae018abee4d1e10036/BUSSINES_LOGO_jpeg",
        "sector": {
            "sectorId": "4028808879868679017986ac3c45000a",
            "englishName": "Technology and telecommunications",
            "spanishName": "Tecnología y telecomunicaciones",
            "keySystem": "MEX"
        },
        "industry": {
            "industryId": "40288088798a3b0501798a58ca500059",
            "englishName": " Software",
            "spanishName": "Software",
            "keySystem": "MEX"
        },
        "typeCompany": {
            "catalogSystemId": "2c9f906e8684a58a0186942003290004",
            "name": "Nacional",
            "type": "typeCompany",
            "status": None,
            "keySystem": "MEX"
        },
        "companySize": "MASDE250",
        "country": "MX",
        "colorTextButton": None,
        "colorText": None,
        "pathLogoEmail": "https://involve-resources.s3.amazonaws.com/res-involve/company-avatar.png",
        "colorButton": None,
        "website": None,
        "description": None,
        "totalCoins": 31,
        "facturapiCustomerId": "6513574809e7add54945062d",
        "facturapiUseCfdi": "D03",
        "vacancyApprove": "NEVER",
        "invoiceNotification": True,
        "legalName": None,
        "address": None,
        "zipCode": None,
        "invoiceCounter": None
    }
}

def nombrePerfil(headers):
    sendPutBody(urlPerfil, headers, body, 200)
    print('se cambiaron los nombres')
