from objetos.funciones import base, eliminarFoto
url = base + 'files/upload/delete-file?typeFile=URL_PHOTO'
def borrarFoto(headers):
    eliminarFoto(url, headers, 200)