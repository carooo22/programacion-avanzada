from datetime import date

class Material:
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible=True):
        self.idMaterial=idMaterial
        self.titulo=titulo
        self.añoPublicacion=añoPublicacion
        self.disponible=disponible

    def coincide_autor(self, autor):
        return False    

    def __str__(self):
        return self.titulo    

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor=autor
        self.isbn=isbn
        self.genero=genero

    def coincide_autor(self, autor):
        return self.autor.lower()==autor.lower()   


class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion=edicion
        self.periodicidad=periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)                
        self.tipoArchivo=tipoArchivo
        self.urlDescarga=urlDescarga
        self.tamañoMB=tamañoMB



class Persona:
    def __init__(self, nombre):
        self.nombre=nombre


class Usuario(Persona):
    def __init__(self, nombre, limitePrestamos):
        super().__init__(nombre)                
        self.limitePrestamos=limitePrestamos
        self.listaActiva=[]

    def revisarpuede_prestamo(self):
        print("\n¿P U E D O   H A C E R   U N   P R E S T A M O?")
        if len(self.listaActiva) < self.limitePrestamos ==True:
            print("puede hacer un prestamo")
        else:
            print("llego al limite de prestamos, no puede realizar otro")    


class Bibliotecario(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def gestionar_prestamo(self, prestamo):
        print("\nG E S T I O N A R   P R E S T A M O")
        print(f"prestamo gestionado:", prestamo.idPrestamo)    

    def transferir_material(self, material, sucursalOrigen, sucursalDestino):
        print("\nT R A N S F E R I R   M A T E R I A L")
        if material in sucursalOrigen.catalogoLocal:
            sucursalOrigen.catalogoLocal.remove(material)
            sucursalDestino.catalogoLocal.append(material)
            print("Material transferido a la sucursal", sucursalDestino.nombre)


class Sucursal:
    def __init__(self, idSucursal, nombre):
        self.idSucursal=idSucursal
        self.nombre=nombre
        self.catalogoLocal=[]




class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo=idPrestamo
        self.fechaInicio=fechaInicio
        self.fechaDevolucion=fechaDevolucion
        self.usuario=usuario
        self.material=material



class Penalizacion:
    def __init__(self, monto, motivo, pagada):
        self.monto=monto
        self.motivo=motivo
        self.pagada=pagada

    def calcular_multa(self, diasRetraso):
        self.monto += diasRetraso * 10
        print("\nC A L C U L A R   M U L T A")
        print (f"el total de su multa es {self.monto}")

    def bloquear_usuario(self, nombre):
        if self.pagada==False:
            print("\nB L O Q U E A R   U N   U S U A R I O")
            print(f"el usuario {nombre} ha sido bloqueado por una multa pendiente")


class Catalogo:
    def __init__(self):
        self.materiales=[]

    def agregar_materiales(self, material):
        self.materiales.append(material)
        print("\nA G R E G A R   M A T E R I A L E S")
        print(f"se agrego el material '{material}' al catalogo")

    def buscar_por_autor(self, autor):
        print("\n B U S Q U E D A   P O R   A U T O R")
        encontrados = []
        print(f"buscando materiales del autor: {autor}")        
        for m in self.materiales:
            if m.coincide_autor(autor):
                encontrados.append(m)
                print(f"encontrado: {m}") 
        
        if not encontrados:
            print("no se encontraron materiales para este autor")            
        return encontrados


    def buscar_todas_sucursales(self, titulo, sucursales):
        print("\nB U S Q U E D A   E N   T O D A S   L A S   S U C U R S A L E S")
        encontrados = []
        print(f"buscando '{titulo}' en todas las sucursales")
        
        for suc in sucursales:
            for mat in suc.catalogoLocal:
                if titulo.lower() in mat.titulo.lower():
                    encontrados.append((mat, suc.nombre))
                    print(f"encontrado: {mat} | ubicación: sucursal {suc.nombre}")        
        if not encontrados:
            print(f"no se encontró ningún material con el título '{titulo}'.")
            
        return encontrados

      