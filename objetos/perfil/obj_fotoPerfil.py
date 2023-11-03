from objetos.funciones import base, foto, subirArchivo, eliminarFoto

url = base + 'files/upload/uploadFile?typeFile=URL_PHOTO'

ruta = foto()
print(ruta)


def fotoPerfil(headers):
    subirArchivo(ruta, url, headers, 201)
    print('Se subio la foto de perfil')




