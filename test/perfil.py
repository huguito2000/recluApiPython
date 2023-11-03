import time
from objetos.perfil.obj_Perfil import nombrePerfil
from objetos.perfil.obj_cambioPass import cambioPass
from objetos.perfil.obj_correo import cambioEmail
from objetos.perfil.obj_eliminarFoto import borrarFoto
from objetos.perfil.obj_fotoPerfil import fotoPerfil
from objetos.perfil.obj_telefono import telefono
from test.login import login
from objetos.funciones import base, foto

url = base + 'files/upload/uploadFile?typeFile=URL_PHOTO'

ruta = foto()
print(ruta)

files = {'file': open(ruta, 'rb')}

headers = login()

# se mandan los nombres cambiados
nombrePerfil(headers)

# se cambia la foto de perfil
fotoPerfil(headers)
time.sleep(1)

# se elimina la foto de perfil
borrarFoto(headers)

# se cambia la foto de perfil
fotoPerfil(headers)

# se cambio el email
cambioEmail(headers)

# se cambio el telefono
telefono(headers)

# se cambia la pass
cambioPass(headers)
