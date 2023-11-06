from objetos.funciones import sendPutBody

url = 'https://pre.micros.involverh.com.mx/management/invoice/customer'
myBody = {
    "legal_name": "HUGO RAFAEL RODRIGUEZ OLIVERA",
    "tax_id": "ROOH881217SZ7",
    "tax_system": "605",
    "email": "huguito.reclutador@yopmail.com",
    "phone": "+525569777077",
    "address": {
        "zip": "56615"
    },
    "id": "6513574809e7add54945062d"
}

def rfc(headers):
    sendPutBody(url, headers, myBody, 200)