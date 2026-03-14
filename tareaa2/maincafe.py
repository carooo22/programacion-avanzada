from modelscafe import *

per1=Persona("Daniel", "dani@mail")
per2=Persona("Caro", "carito@mail")
per3=Persona("may", "may@mail")
per4=Persona("rosalba", "rosi@mail")
per5=Persona("pablo","pablo@mail")
per6=Persona("danae", "danae@mail")
per7=Persona("elena", "elenita@mail")
per8=Persona("fer", "fer@mail")
per9=Persona("jin", "jin@mail")
per10=Persona("ilse", "ilse@mail")

print("\n I N I C I O   D E   S E S I O N")
per1.login()
per2.login()
per1.logout()

print("\n A C T U A L I Z A R   D A T O S")
per6.act_datos("dana@mail")
per7.act_datos("elena@mail")


bebi1=Bebida(12, "cafe moka", 50, "mediano", "fria")
bebi2=Bebida(13, "cafe americano", 35, "pequeño", "caliente")
bebi3=Bebida(14, "granizado de mango", 30, "mediano", "fria")
bebi4=Bebida(15, "chocolate", 65, "grande", "caliente")
bebi5=Bebida(16, "frappe de oreo", 60, "mediano", "fria")
bebi6=Bebida(17, "latte", 50, "mediano", "caliente")
bebi7=Bebida(18, "agua simple", 20, "500ml", "fria")
bebi8=Bebida(19, "té", 20, "mediano", "caliente")
bebi9=Bebida(20, "té", 20, "mediano", "fria")
bebi10=Bebida(21, "jugo naranja", 25, "pequeño", "fria")


pos1=Postre(0, "galleta", 30, True, False)
pos2=Postre(1, "panque chocolate", 40, False, True)
pos3=Postre(2, "cheesecake vasco", 60, True, False)
pos4=Postre(3, "flan de coco", 40, False, True)
pos5=Postre(4, "banana bread", 45, True, False)
pos6=Postre(5, "panna cotta", 50, False, True)
pos7=Postre(6, "helado de fruta de temporada", 30, True, False)
pos8=Postre(7, "tarta de chocolate", 40, False, True)
pos9=Postre(8, "carrot cake", 55, True, False)
pos10=Postre(9, "mousse de chocolate", 45, True, False)

pedi1=Pedido(1111)
pedi2=Pedido(2222)
pedi3=Pedido(3333)
pedi4=Pedido(4444)
pedi5=Pedido(5555)
pedi6=Pedido(6666)
pedi7=Pedido(7777)
pedi8=Pedido(8888)
pedi9=Pedido(9999)
pedi10=Pedido(1010)


emple1=Empleado("Carolina", "carolina@mail", 22, "gerente")
emple2=Empleado("May", "may@mail", 77, "barista")
emple3 = Empleado("Julián", "julian@mail", 35, "mesero")
emple4 = Empleado("Sofía", "sofia@mail", 29, "mesero")
emple5 = Empleado("Ricardo", "ricardo@mail", 42, "barista")
emple6 = Empleado("Elena", "elena@mail", 31, "barita")
emple7 = Empleado("Marcos", "marcos@mail", 50, "meseror")
emple8 = Empleado("Lucía", "lucia@mail", 24, "mesero")
emple9 = Empleado("Daniel", "daniel@mail", 38, "gerente")
emple10 = Empleado("Valeria", "valeria@mail", 45, "barista")


print("\n I N V E N T A R I O")
inventario = Inventario()
inventario.ingredientes = {
        "cafe": 10,
        "leche": 8,
        "azucar": 15,
        "chocolate": 6,
        "harina": 8,
        "huevos":20,
        "leche avena": 5,
        "naranjas":10,
        "fresas": 2,
        "vainilla":3
    }

emple1.actualizar_inventario(inventario, "leche", 10)

inventario.reducir_stock("azucar", 5)
inventario.reducir_stock("leche", 8)

inventario.notificar_faltante("leche")


cli1=Cliente("daniel", "daniel@mail")




print("\n T O T A L")
pedi1.agregar_producto(bebi1)
bebi1.ver_bebida()
bebi1.agregar_extra("vainilla", 5)
pedi1.calcular_total()
emple1.cambiar_estadoPedido(pedi1, estadoPedido.PREPARANDO)


print("\n T O T A L")
pedi2.agregar_producto(bebi10)
pedi2.agregar_producto(pos10)
bebi10.ver_bebida()
pedi2.calcular_total()
emple2.cambiar_estadoPedido(pedi1, estadoPedido.PENDIENTE)

print("\n T O T A L")
pedi3.agregar_producto(bebi1)
pedi3.agregar_producto(pos5)
bebi1.ver_bebida()
pedi3.calcular_total()
emple1.cambiar_estadoPedido(pedi3, estadoPedido.PREPARANDO)

print("\n T O T A L")
pedi4.agregar_producto(bebi5)
pedi4.agregar_producto(pos2)
bebi5.ver_bebida()
bebi5.agregar_extra("sin azucar", 0)
pedi4.calcular_total()
emple2.cambiar_estadoPedido(pedi4, estadoPedido.ENTREGADO)

print("\n T O T A L")
pedi5.agregar_producto(pos3)
pedi5.agregar_producto(bebi3)
bebi3.ver_bebida()
pedi5.calcular_total()
emple1.cambiar_estadoPedido(pedi5, estadoPedido.PENDIENTE)

print("\n T O T A L")
pedi6.agregar_producto(bebi2)
pedi6.agregar_producto(pos4)
bebi2.ver_bebida()
pedi6.calcular_total()
emple2.cambiar_estadoPedido(pedi6, estadoPedido.PENDIENTE)

print("\n T O T A L")
pedi7.agregar_producto(pos10)
pedi7.agregar_producto(bebi7)
bebi5.ver_bebida()
pedi7.calcular_total()
emple1.cambiar_estadoPedido(pedi7, estadoPedido.ENTREGADO)

print("\n T O T A L")
pedi8.agregar_producto(pos1)
pedi8.agregar_producto(bebi2)
bebi6.ver_bebida()
pedi8.calcular_total()
emple2.cambiar_estadoPedido(pedi8, estadoPedido.PREPARANDO)

print("\n T O T A L")
pedi9.agregar_producto(bebi8)
bebi8.ver_bebida()
pedi9.calcular_total()
emple1.cambiar_estadoPedido(pedi9, estadoPedido.PENDIENTE)

print("\n T O T A L")
pedi10.agregar_producto(pos8)
pedi10.calcular_total()
emple2.cambiar_estadoPedido(pedi10, estadoPedido.ENTREGADO)