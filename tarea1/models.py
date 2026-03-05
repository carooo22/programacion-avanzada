from enum import Enum

#////////////////////
#  E M U M
#////////////////////

class rolEmpleado(Enum):
    TAQUILLERO="taquillero"
    ADMIN="admin"
    LIMPIEZA="limpieza"

class tipoSala(Enum):
    DOSD= "2D"
    TRESD= "3D"
    IMAX= "IMAX"

class estadoReserva(Enum):
    PENDIENTE="pendiente"
    PAGADA="pagada"
    CANCELADA="cancelada"       



#////////////////////
#  E S P A C I O S
#////////////////////

class espacio:
    def __init__(self, id_espacio, nombre, ubi):
        self.id_espacio=id_espacio
        self.nombre=nombre
        self.ubi=ubi


class sala(espacio):
    def __init__(self, id_espacio, nombre, ubi, tipo, capacidad):
        super().__init__(id_espacio, nombre, ubi)
        self.tipo = tipo
        self.capacidad = capacidad
        self.asientos_ocupados= []

    def ver_dispo(self):
        disponibles = self.capacidad-len(self.asientos_ocupados)
        if disponibles==0:
            print(f"no hay asientos disponibles en {self.nombre}")
        else:
            print(f"hay {disponibles} asientos disponibles en {self.nombre} de un total de {self.capacidad}")    
        

class zonaComida(espacio):
    def __init__(self, id_espacio, nombre, ubi, stock):
        super().__init__(id_espacio, nombre, ubi)
        self.stock=stock
        self.productos={}

    def vender_producto(self, nombre, cantidad):
        if nombre in self.productos and self.productos[nombre]>=cantidad:
            self.productos[nombre]-=cantidad
            print(f"se vendieron {cantidad} unidades del producto: {nombre}")
        else:
            print(f"no hay stock del producto: {nombre}, actualice el stock")   
           

    def actualizar_stock(self, nombre, cantidad):
        if(self.stock+cantidad)<0:
            print("no hay suficiente stock")
        else:
            self.stock+=cantidad 
            print(f"el nuevo stock del producto {nombre} es {cantidad}")    



#////////////////////
#  P E R S O N A
#////////////////////

class persona:
    def __init__(self, nombre, email, tel):
       self.nombre = nombre
       self.email = email
       self.tel = tel

    def login(self):
        print(f"{self.nombre} ha iniciado sesion")

    def logout(self):
        print(f"{self.nombre} ha cerrado su sesion")

    def act_datos(self, email, tel):
        self.email=email
        self.tel=tel



#////////////////////
#  E M P L E A D O
#////////////////////

class empleado(persona):
    def __init__(self, nombre, email, tel, id_emple, rol, horario):
        super().__init__(nombre, email, tel)
        self.id_emple=id_emple
        self.rol=rol
        self.horario=horario

    def marcar_entrada(self):
        print(f"{self.nombre} marco su entrada")

    def gestionar_funciones(self):
        if self.rol== rolEmpleado.ADMIN.value:
            print(f"{self.nombre} esta gestionando funciones")
        else:
            print(f"{self.nombre} no tienes acceso a la gestion de funciones")        



#////////////////////
#  F U N C I O N
#////////////////////

class funcion:
    def __init__(self, id_funcion, pelicula, sala, hora_inicio, precio_base):
        self.id_funcion=id_funcion
        self.pelicula=pelicula
        self.sala=sala
        self.hora_inicio=hora_inicio
        self.precio_base=precio_base

    def calcular_asientos_dispo(self):
        self.sala.ver_dispo()         



#////////////////////
#  P E L i C U L A
#////////////////////

class pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero



# ////////////////////
#  U S U A R I O
# ////////////////////

class usuario(persona):
    def __init__(self, nombre, email, tel):
        super().__init__(nombre, email, tel)
        self.puntos_fidelidad = 0
        self.historial_reservas = []

    def crear_reserva(self, funcion_instancia, asientos):
        nueva_reserva = reserva(len(self.historial_reservas) + 1, self, funcion_instancia, asientos)
        self.historial_reservas.append(nueva_reserva)
        return nueva_reserva

    def cancelar_reserva(self, reserva_instancia):
        reserva_instancia.estado = estadoReserva.CANCELADA


# ////////////////////
#  P R O M O C I O N
# ////////////////////

class promocion:
    def __init__(self, codigo, descuento, fecha_expiracion):
        self.codigo = codigo
        self.descuento = descuento
        self.fecha_expiracion = fecha_expiracion

    def aplicar_descuento(self, monto):
        return monto - (monto * self.descuento)


# ////////////////////
#  R E S E R V A
# ////////////////////

class reserva:
    def __init__(self, id_reserva, usuario, funcion, asientos):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.estado = estadoReserva.PENDIENTE
        self.monto_total = len(asientos) * funcion.precio_base

        self.funcion.sala.asientos_ocupados.extend(asientos)

    def confirmar_pago(self):
        self.estado = estadoReserva.PAGADA


    def aplicar_promocion(self, promo):
        self.monto_total = promo.aplicar_descuento(self.monto_total)