import null
from objetos.funciones import base, nombres, apellidos

urlPerfil = base + 'user/recruiter/'

nombre = nombres()
apellidoP = apellidos()
apellidoM = apellidos()
body = {
    "recruiterId": "ff8080818ab932ae018abee4d1ea0037",
    "status": "PENDIENTE",
    "showModalPause": False,
    "vacantsActived": -16,
    "nextDailyReport": null,
    "lastDailyReport": null,
    "stepsStatus": 8,
    "positionCompany": "Reclutador",
    "crmLeadId": 32268,
    "vacantsTotal": null,
    "user": {
        "userId": "ff8080818ab932ae018abee4d1ea0038",
        "name": {nombre},
        "lastName": {apellidoP},
        "checkCode": "2280",
        "secondLastName": {apellidoP},
        "email": "huguito.reclutador@yopmail.com",
        "emailVerify": "2023-09-26 16:55:11",
        "phoneVerify": null,
        "password": "$2a$10$9wAYcqxkO4yErmGB7RyGgujJvsuzCGeQIm4VSNtaC8L1pXjX8dBBu",
        "gender": null,
        "photo": "https://s3.us-east-1.amazonaws.com/involve-resources-dev-pre/RECRUITER/ff8080818ab932ae018abee4d1ea0037/URL_PHOTO_jpeg?1698792585223?1698792623512",
        "phone": "+525569777077",
        "attempts": 0,
        "userRol": "RECRUITER_ADMIN",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "acceptNewsletter": False,
        "acceptCookies": True,
        "createDate": "2023-09-22 15:56:22",
        "lastActivity": "2023-10-31 16:49:18",
        "stripeCustomerId": "cus_OgeeGe8OGKpXVz",
        "keySystem": "MEX",
        "urlRegister": null,
        "historyDevices": [],
        "notifications": []
    },
    "company": {
        "companyId": "ff8080818ab932ae018abee4d1e10036",
        "company": null,
        "businessName": "involve",
        "rfc": null,
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
            "status": True,
            "keySystem": "MEX"
        },
        "companySize": "MASDE250",
        "country": "MX",
        "colorTextButton": null,
        "colorText": null,
        "pathLogoEmail": "https://involve-resources.s3.amazonaws.com/res-involve/company-avatar.png",
        "colorButton": null,
        "website": null,
        "description": null,
        "totalCoins": 31,
        "facturapiCustomerId": "6513574809e7add54945062d",
        "facturapiUseCfdi": "D03",
        "vacancyApprove": "NEVER",
        "invoiceNotification": True,
        "legalName": null,
        "address": null,
        "zipCode": null,
        "invoiceCounter": null
    }
}