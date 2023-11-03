from objetos.funciones import base, sendPostHeadersSinBody

url = base + 'notification/session-aux/change-email?newEmail=huguito.reclutador1@yopmail.com&password=Abcd.1234'

def cambioEmail(headers):
    sendPostHeadersSinBody(url, headers, 200)