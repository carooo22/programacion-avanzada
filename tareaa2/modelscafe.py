from enum import Enum

class rolEmpleado(Enum):
    BARISTA="barista"
    MESERO="mesero"
    GERENTE="gerente"

class tempeBebida(Enum):
    FRIA = "fria"
    CALIENTE = "caliente"

class estadoPedido(Enum):
    PENDIENTE="pendiente"
    PREPARANDO="preparando"
    ENTREGADO="entregado"  



class Persona:
    def __init__(self, nombre, email):
       self.nombre = nombre
       self.email = email

    def login(self):
        print(f"{self.nombre} ha iniciado sesion")

    def logout(self):
        print(f"{self.nombre} ha cerrado su sesion")

    def act_datos(self, nuevo_email):
        self.nuevo_email=nuevo_email
        print(f"{self.nombre} ha actualizado su correo: {nuevo_email}")


class Cliente(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.puntos_fide=0
        self.histo_pedidos=[]

    def realizar_pedido(self):    
        self.histo_pedidos.append(pedido)
        print("pedido agregado al historial")

    def consultarHistorial(self):
        for pedido in self.histo_pedidos:
            print("pedido:", pedido.id_pedido, "total:", pedido.total)

    def canjearPuntos(self):
        if self.puntos_fide >= 100:
            print("canjeaste un premio")
            self.puntos_fide -= 100
        else:
            print("no tienes suficientes puntos")
   

class Empleado(Persona):
    def __init__(self, nombre, email, id_empleado, rol):
        super().__init__(nombre, email)
        self.id_empleado=id_empleado
        self.rol=rol

    def actualizar_inventario(self, inventario, ingrediente, cantidad):
        inventario.ingredientes[ingrediente] = cantidad
        print("Inventario actualizado")

    def cambiar_estadoPedido(self, pedido, estado):
        pedido.estado = estado
        print("Estado del pedido cambiado a:", estado.value)


class ProductoBase:
    def __init__(self, id_produc, nombre, precio_base):
        self.id_produc=id_produc
        self.nombre=nombre
        self.precio_base=precio_base

    def precio_final(self):
        return self.precio_base

class Bebida(ProductoBase):
    def __init__(self, id_produc, nombre, precio_base, tamaño, temperatura):
        super().__init__(id_produc, nombre, precio_base)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.lista_modificadores = []

    def agregar_extra(self, n_extra, precio_delextra):
        self.lista_modificadores.append((n_extra, precio_delextra))
        print(f"agregaste {n_extra} a tu {self.nombre} y tiene un costo de ${precio_delextra}")

    def ver_bebida(self):
        precio = self.precio_final()
        if precio == self.precio_base:
            print(f"su bebida es {self.nombre} de tamaño {self.tamaño}, es {self.temperatura} y tiene un costo de ${self.precio_base}")
        else:
            print(f"su bebida es {self.nombre} de tamaño {self.tamaño}, es {self.temperatura} y el precio final es ${precio}")

    def precio_final(self):
        total=self.precio_base
        for x in self.lista_modificadores:
             total+=x[1]
        return total     

    def __repr__(self):
        return f"{self.nombre}"

class Postre(ProductoBase):
    def __init__(self, id_produc, nombre, precio_base, esVegano, sinGluten):
        super().__init__(id_produc, nombre, precio_base)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

    def __repr__(self):
        return f"{self.nombre}"    



class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido=id_pedido
        self.estado = estadoPedido.PENDIENTE
        self.total=0
        self.productoscomprados = []

    def agregar_producto(self, producto):
        self.productoscomprados.append(producto)
        print(F"agrego {self.productoscomprados} a su pedido")

    def calcular_total(self):
        total = 0

        for producto in self.productoscomprados:
                total += producto.precio_final()

        self.total=total
        print (f"el total de su pedido es de {self.total}")



class Inventario:
    def __init__(self):
        self.ingredientes = {}

    def reducir_stock(self, ingrediente, cantidad):

        if ingrediente in self.ingredientes:

            self.ingredientes[ingrediente] -= cantidad

            if self.ingredientes[ingrediente] < 5:
                self.notificar_faltante(ingrediente)

    def notificar_faltante(self, ingrediente):
        print("falta ingrediente:", ingrediente)
