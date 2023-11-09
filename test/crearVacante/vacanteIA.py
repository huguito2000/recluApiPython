from objetos.crearVacante.obj_vacanteIA import crearVacanteIA
from test.login1 import login

def CrearVacanteIA():
    try:
        respuesta, headers, recruiterID = login()
        crearVacanteIA(headers)
        print('Se creo la vacante por IA')
        return 'se creo la vacante por IA'
    except Exception as e:
        print('No se cro la vacante por IA', str(e))
        return 'No se creo la vacante por IA'
