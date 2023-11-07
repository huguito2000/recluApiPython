import time
from objetos.ajustes.perfil.obj_Perfil import nombrePerfil
from objetos.ajustes.perfil.obj_cambioPass import cambioPass
from objetos.ajustes.perfil.obj_correo import cambioEmail
from objetos.ajustes.perfil.obj_eliminarFoto import borrarFoto
from objetos.ajustes.perfil.obj_fotoPerfil import fotoPerfil
from objetos.ajustes.perfil.obj_telefono import telefono
from test.login1 import login
from objetos.ajustes.obj_empresa import empresa
from objetos.ajustes.obj_facturacion import rfc
from objetos.ajustes.obj_EquipoReclutamiento import invitacion

headers, recruiterID = login()

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

# se manda request empresa
empresa(headers)

# se manda requets de facturacion
rfc(headers)

# se manda request de equipo de reclutamiento

invitacion(headers)
