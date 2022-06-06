from manejador import ManejaFacultades

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {'1': self.opcion1,
                           '2': self.opcion2,
                           '3': self.salir}

    def opcion(self, op, manejador):
        func = self.__switcher.get(op, lambda: print('Opcion no valida'))
        if (op == '1' or op == '2'):
            func(manejador)
        else:
            func()

    def opcion1(self, manejador):
        if type(manejador) == ManejaFacultades:
            manejador.BuscarFacultad()

    def opcion2(self, manejador):
        if type(manejador) == ManejaFacultades:
            manejador.BuscaCarrera()

    def salir(self):
        print('terminado!')
