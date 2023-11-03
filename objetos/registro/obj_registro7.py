from objetos.funciones import base, sendPatch
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

#se manda PATCH del formulario de compañia
def reg7(headers):
    sendPatch(urlCompany, headers, company, 200)
    print('se manda la compañia')