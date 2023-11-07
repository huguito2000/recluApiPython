from objetos.crearVacante.obj_vacanteIA import crearVacanteIA
from test.login1 import login

headers, recruiterID = login()
crearVacanteIA(headers)