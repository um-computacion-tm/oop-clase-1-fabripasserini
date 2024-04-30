class Alumno:
    
    def __init__(self, el_nombre_del_alunmo):
        self.__nombre__ = el_nombre_del_alunmo
        self.__inasistencia__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def falta(self):
        self.__inasistencia__ += 1
    def esta_libre(self):
        if self.__inasistencia__ >= 5:
            return "ESTA LIBRE"
        else:
            return "NO ESTA LIBRE"
    def elegir_dieta_especia(self, la_dieta):
        self.__dieta__ = la_dieta
    def es_vegano(self):
        self.__dieta__ = "vegano"
    def mentoria(self, profesor):
        self.__mentor__ = profesor 