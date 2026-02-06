class Producto():
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def aplicar_descuento(self, porcentaje):
        self.precio*=(1-porcentaje)
        print(f"el nuevo precio del producto {self.nombre} es {self.precio} pesos")

    def actualizar_stock(self, cantidad):
        if(self.stock+cantidad)<0:
            print("no hay suficiente stock")
        else:
            self.stock+=cantidad 
            print(f"el nuevo stock del producto {self.nombre} es {self.stock}")

class categoria():
    def __init__(self, nombre):
        self.nombrecat=nombre
        self.lista=[]

    def agregar_producto(self, nuevoproducto):
        self.lista.append(nuevoproducto)
        print(f"el nuevo producto es {nuevoproducto.nombre}")

    def valor_total_categoria(self):
        suma=0
        for d in self.lista:
            suma+=d.precio*d.stock
        print(f"el precio total de la categoria {self.nombrecat} es {suma} pesos")        