from objetos.funciones import base, foto, subirArchivo

def fotoPerfil(headers):
    url = base + 'files/upload/uploadFile?typeFile=URL_PHOTO'

    ruta = foto()
    print(ruta)

    subirArchivo(ruta, url, headers, 201)
    print('Se subio la foto de perfil')




