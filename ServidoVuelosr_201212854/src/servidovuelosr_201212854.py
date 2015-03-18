from SimpleXMLRPCServer import SimpleXMLRPCServer
class Humano:
    
    edad=None
    nombres=None
    
    def __init__(self,edades,nombre):
        self.edad=edades
        self.nombres=nombre
        print "Soy un nuevo objeto"
        
            
    def hablar(self,mensaje):
        print mensaje
        
    def getNombre(self):
        return self.nombres

    def getEdad(self):
        return self.edad
    
class Nodos:
    
       
    def __init__(self,indice,dato,dato2,dato3,dato4,dato5,dato6,dato8,dato9,dato10,dato11):
        self.siguiente=None
        self.anterior=None
        self.info=dato
        self.info2=dato2
        self.info3=dato3
        self.info4=dato4
        self.info5=dato5
        self.info6=dato6
        self.info8=dato8
        self.info9=dato9
        self.info10=dato10
        self.info11=dato11
        self.ind=indice
   
    def VerNodo(self):
        return self.info
    
    def VerNodo2(self):
        return self.info2
    
    def VerNodo3(self):
        return self.info3
    
    def VerNodo4(self):
        return self.info4
    
    def VerNodo5(self):
        return self.info5
    
    def VerNodo6(self):
        return self.info6
    
    def VerNodo7(self):
        return self.ind
    
    def VerNodo8(self):
        return self.info8
    
    def VerNodo9(self):
        return self.info9
    
    def VerNodo10(self):
        return self.info10
    
    def VerNodo11(self):
        return self.info11
    
    
class Lista:
    
    def __init__(self):
        self.cabeza=None
        self.cola=None
        
        
    def vacia(self):
        if self.cabeza==None:
           return True
        else:
            return False
        
    def InsertarPrimero(self,indice,dato,dato2,dato3,dato4,dato5,dato6,dato8,dato9,dato10,dato11):
        temporal=Nodos(indice,dato,dato2,dato3,dato4,dato5,dato6,dato8,dato9,dato10,dato11)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
        else:
            temporal.siguiente=self.cabeza
            self.cabeza.anterior=temporal
            self.cabeza=temporal
            
    def listar(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo7()==str(no):    
                return temporal.VerNodo()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
           
    def listarCateg(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo7()==str(no):    
                return temporal.VerNodo2()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
    
    def listarAerop(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo7()==str(no):    
                return temporal.VerNodo2()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
           
    def listarAeropDeVuelos(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo()==str(no):    
                return temporal.VerNodo4()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente 
           
    def listarPasajeros(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo()==str(no):    
                return temporal.VerNodo9()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
    def listarPasajerosTurista(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo()==str(no):    
                return temporal.VerNodo10()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
           
    def listarPasajerosEjecutiva(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo()==str(no):    
                return temporal.VerNodo11()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente       
           
    def listarEstado(self,no):
        print("********"+no)
        temporal=self.cabeza
        while temporal!=None:
           if temporal.VerNodo7()==str(no):    
                return temporal.VerNodo8()
                #print("Existe"+temporal.VerNodo())
               #print temporal.VerNodo2()
            #else:
             #   print "No exitste"
           temporal=temporal.siguiente
            
    def EnviarDatos(self):       
        return listar()
            
    def listarDesdeCola(self):
        print("********")
        temporal=self.cola
        while temporal!=None:
            print(temporal.VerNodo())
            temporal=temporal.anterior
            
    def borrarPrimero(self):
        if self.vacia()==False:
            self.cabeza=self.cabeza.siguiente
            self.cabeza.anterior=None
            
    def borrarUltimo(self):
        if self.cola.anterior==None:
            self.cabeza=None
            self.cola=None
        else:
            self.cola.anterior
            self.cola.siguiente=None
            
    def borrarPosicion(self,pos):
        anterior=self.cabeza
        actual=self.cabeza
        k=0
        if pos > 0:
            while k!=pos and actual.siguiente!=None:
                anterior=actual
                actual=actual.siguiente
                k+=1
            if k==pos:
                temporal=actual.siguiente
                anterior.siguiente=actual.siguiente
                temporal.anterior=anterior
#----------------------------------------------------------------------------------------FIN LISTA DOBLEMENTE ENLZADA

#INICIO ARBOL AVL------------------------------------------------------------------------
class Nodo :
	def __init__(self, dato, izq=None, der=None):
		self.dato = dato
		self.altura = 0
		self.izq = izq
		self.der = der

def altura(nodo): 
	if(nodo):
		return nodo.altura
	else:
		return -1

def actualizarAltura(nodo):
	if (not nodo): return
	nodo.altura = max(altura(nodo.izq), altura(nodo.der)) +1

#rotaciones
def rotarS(nodo, a_izq):
	
	n2 = None
	if (a_izq):#rotacion izquierda
		n2 = nodo.izq
		nodo.izq = n2.der
		n2.der = nodo
	else:#rotacion derecha
		n2 = nodo.der
		nodo.der = n2.izq
		n2.izq = nodo
	actualizarAltura(nodo)
	actualizarAltura(n2)
	return n2 #no hay pasaje por referencia en python (de manera limpia)

def rotarD(nodo, a_izq):
	if(a_izq):
		nodo.izq = rotarS(nodo.izq, False)
		nodo = rotarS(nodo, True)
	else:
		nodo.der = rotarS(nodo.der, True)
		nodo = rotarS(nodo, False)
	return nodo
	
def balancear(nodo):
	if (not nodo): return
	if altura(nodo.izq) - altura(nodo.der) == 2:#podria almacenar el resultado de la diferencia pero asi se entiende mas
		#desequilibrio hacia la izquierda
		if altura(nodo.izq.izq) >= altura(nodo.izq.der):
			#desequilibrio simple a la izq
			nodo = rotarS(nodo, True)
		else:
			#desequilibrio doble a la izquierda
			nodo = rotarD(nodo, True)
	elif altura(nodo.der) - altura(nodo.izq) == 2:
		#desequilibrio hacia la derecha
		if altura(nodo.der.der) >= altura(nodo.der.izq): 
			#desequilibrio simple hacia la derecha
			nodo = rotarS(nodo, False)
		else:
			#desequilibrio doble hacia la derecha
			nodo = rotarD(nodo, False)
	return nodo

def insertar(nodo, dato):
	if (not nodo) :
		nodo = Nodo(dato, None, None)
	else:
		#la magia de la recursividad hace todo aca
		if (dato < nodo.dato):
			nodo.izq = insertar(nodo.izq, dato)
		else:
			nodo.der = insertar(nodo.der, dato)
		nodo = balancear(nodo)
		actualizarAltura(nodo)
	return nodo

space = 5
v_space = 1 
grafo=""
def mostrar(nodo):  
        global grafo
        if (not nodo):
           return " "
        if (nodo.izq!=None):            
           grafo+=str(nodo.dato)+"->"+str(nodo.izq.dato)+"\n"
           if (str(nodo.dato=="x")):
               print "Encontrado"+str(nodo.dato)
           mostrar(nodo.izq)
        if (nodo.der!=None):
           grafo+=str(nodo.dato)+"->"+str(nodo.der.dato)+"\n"
           mostrar(nodo.der)

        return(grafo)
    
           
def mo(n):
    print n

def lvlnode(nodo, dlvl, lvl =0):
	if (lvl == dlvl): 
		return [nodo]#if nodo is None will return None (important)
	#return empty only if is not the level im looking 4
	if (lvl < dlvl):
		nodes = []
		izq = nodo and nodo.izq #this forces to add a None when the node doesnt exists and there is another level
		der = nodo and nodo.der
		nodes += lvlnode(izq, dlvl, lvl+1)
		nodes += lvlnode(der, dlvl, lvl+1)
		return nodes 
#-----------------------------------------------------------------------------------------FIN ARBOL AVL
server = SimpleXMLRPCServer(('localhost', 9000), allow_none=True)
listas=Lista()
listaAero=Lista()
listaVuelo=Lista()
listaCategoria=Lista()
nodos=Nodo("fr",None,None)
# Expose a function

raiz = None
def sins(dato): #simple insertar
	global raiz
	raiz = insertar(raiz, dato)
        return mostrar(raiz)


def list_contents(name):
    return name+' Vuelos'

def suma(x,y):
    return x+y


def ListaDoble(indice,dato,dato2,dato3,dato4,dato5,dato6):
    listas.InsertarPrimero(indice,dato,dato2,dato3,dato4,dato5,dato6," "," "," ")
  
def MostrarLista(name):
     #listas.listar(name)
     return listas.listar(str(name))
    
def ListaAeropuerto(indice,dato,dato2,dato3):
    listaAero.InsertarPrimero(indice,dato,dato2,dato3," "," "," "," "," "," "," ")

def MostrarListaAero(name):
     #listas.listar(name)
     return listaAero.listar(str(name))
    
def ListaVuelos(indice,dato,dato2,dato3,dato4,dato5,dato6,dato8,dato9,dato10,dato11,dato12,dato13):    
    listaVuelo.InsertarPrimero(indice,dato,dato2,dato3,dato4,dato5,dato6,"En Aeropuerto","Primera Clase: "+dato8+" Costo: "+dato11,"Clase Turista: "+dato9+" Costo: "+dato12,"Clase Ejecutiva: "+dato10+" Costo: "+dato13)
    
def MostrarListaVuelo(name):
    return listaVuelo.listar(str(name))

def MostrarVueloAero(name):
    return listaVuelo.listarAerop(str(name))

def MostrarEstadoVuelo(name):
    return listaVuelo.listarEstado(str(name))

def MostrarAeropuertoDeVuelos(name):
    return listaVuelo.listarAeropDeVuelos(str(name))
    
def ListaCategoria(idVuelo,clase,cantidad,costo):
    listaCategoria.InsertarPrimero(idVuelo,clase,cantidad,costo," "," "," "," "," "," ")
    
def MostrarListaCategoria(name):    
    return listaVuelo.listarPasajeros(str(name))
    
def MostrarListaCategoria2(name):    
    return listaVuelo.listarPasajerosTurista(str(name))    
  
def MostrarListaCategoria3(name):    
    return listaVuelo.listarPasajerosEjecutiva(str(name))    
        
    
server.register_function(list_contents)
server.register_function(suma)
server.register_function(ListaDoble)
server.register_function(MostrarLista)
server.register_function(sins)
server.register_function(ListaAeropuerto)
server.register_function(MostrarListaAero)
server.register_function(ListaVuelos)
server.register_function(MostrarListaVuelo)
server.register_function(MostrarVueloAero)
server.register_function(MostrarEstadoVuelo)
server.register_function(MostrarAeropuertoDeVuelos)
server.register_function(ListaCategoria)
server.register_function(MostrarListaCategoria)
server.register_function(MostrarListaCategoria2)
server.register_function(MostrarListaCategoria3)



try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'
