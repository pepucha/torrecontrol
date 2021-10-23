class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia, va a usarse para crear la cola para arribar y la cola para partir'''
        self.items = []

    def encolar(self, x):
        '''Encola el vuelo a la lista que corresponda'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return len(self.items) == 0

class TorreDeControl(Cola):

    def __init__(self):
        self.lista_arribo = Cola()  #Se inicializa el objeto lista_arribo de tipo Cola(), este a su vez es tambien un atributo.
        self.lista_partida = Cola() #Se inicializa el objeto lista_partida de tipo Cola(), este a su vez es tambien un atributo.

    def nuevo_arribo(self, vuelo):
        '''Para crear una lista de vuelos que van a aterrizar, llamamos al atributo lista_arribo que utiliza el metodo heredado
        encolar() de la clase Cola()
         '''
        self.lista_arribo.encolar(vuelo)

    def nueva_partida(self, vuelo):
        '''Para crear una lista de vuelos que van a salir, llamamos al atributo lista_partida que utiliza el metodo heredado
        encolar() de la clase Cola()
        '''
        self.lista_partida.encolar(vuelo)

    def asignar_pista(self):
        '''Desencola en orden de prioridades, siendo lista_arribo de prioridad.. si tiene vuelos desencola la misma.
        Sino desencola lista_partida.
        Sino hay vuelos en cola, avisa que no hay vuelos en espera'''

        if self.lista_arribo.esta_vacia() and self.lista_partida.esta_vacia() :
            print('No hay vuelos en espera.')
        else:
            if self.lista_arribo.esta_vacia():
                print (f'Vuelos esperando para partir: {self.lista_partida.desencolar()}')
            else:
                print (f'Vuelos esperando para aterrizar: {self.lista_arribo.desencolar()}')

    def ver_estado(self):
        print(f'{self.lista_arribo.items}') #Imprime la lista de vuelos por arribar.
        print(f'{self.lista_partida.items}') #Imprime la lista de vuelos por arribar.


if __name__ == '__main__':
#Se crea un objeto ezeiza de tipo TorreDeControl() que va a tener los atributos:
#lista_arribo y lista_partida y estos heredan los atributos de la clase Cola()
    ezeiza = TorreDeControl()

    ezeiza.nuevo_arribo('Vuelo1')
    ezeiza.nuevo_arribo('Vuelo2')
    ezeiza.nueva_partida('Vuelo3')
    ezeiza.ver_estado()
    ezeiza.asignar_pista()
    ezeiza.ver_estado()
    ezeiza.asignar_pista()
    ezeiza.ver_estado()
