class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email
    def dame_tu_nombre(self):
        return self.__nombre__
