class nodo_lista:

    def __init__(self, tiempo, ref, nitE, nitR, valor, iva, tot, estado):#estado 0=buena 1=error
        self.tiempo=tiempo
        self.ref=ref
        self.nitE=nitE
        self.nitR=nitR
        self.valor=valor
        self.iva=iva
        self.tot=tot
        self.estado=estado
        self.siguiente=None
        self.anterior=None

class lista_doble:
    def __init__(self):
        self.inicio=None
    
    def crear(self, tiempo, ref, nitE, nitR, valor, iva, tot, estado):
        
        nuevo=nodo_lista(tiempo, ref, nitE, nitR, valor, iva, tot, estado)

        if(self.inicio == None):
            self.inicio=nuevo
            self.inicio.siguiente=None
            self.inicio.anterior=None
        else:
            aux=self.ultimaPos
            aux.siguiente=nuevo
            nuevo.anterior=aux
            

    def ultimaPos(self):

        regreso=self.inicio        
        while regreso != None:
            regreso=regreso.siguiente        
        return regreso




