from models import *

#1 persona
persona1=persona("Daniel", "daniel@mail", "222-1234")
print(persona1.nombre)
persona1.login()

#2
empleado1=empleado("caro", "caro@mail", "222-2345", "emplec2", "admin", "10:00 a.m. - 4:00 p.m")
print(empleado1.nombre)
empleado1.login()
empleado1.gestionar_funciones()

empleado2=empleado("may", "may@mail", "222-3456", "emplem8", "taquillero", "10:00 a.m - 8:00 p.m.")
empleado2.login()
empleado2.gestionar_funciones()


# usuario
usuario1 = usuario("daniel", "daniel@mail", "222-1234")


print("\nZONA DE COMIDA")
cine_dulceria = zonaComida(201, "dulceria", "plata baja", 500)
cine_dulceria.productos = {"palomitas": 20, "refrescos": 15, "nachos": 10}

print(f"Inventario inicial: {cine_dulceria.productos}")

cine_dulceria.vender_producto("nachos", 2)
cine_dulceria.actualizar_stock("nachos", 5) 
print(f"{usuario1.nombre} compro demasiadas palomitas")

cine_dulceria.vender_producto("palomitas", 50)
print(f"\nInventario final de productos: {cine_dulceria.productos}")



#sala
sala_imax = sala(1, "sala IMAX", "planta 1", tipoSala.IMAX, 50)

#pelicula
peli = pelicula("avengers: endgame", 180, "B", "accion")

# función
funcion_noche = funcion(101, peli.titulo, sala_imax, 21, 150)


#promoción
promo_estudiante = promocion("ESTU10", 0.10, "31.03.26")

print("\n \nESTADO INICIAL DE LA RESERVA")
funcion_noche.calcular_asientos_dispo()

print("\nPROCESO DE RESERVA")
asientos_usuario= [15, 16, 17]
nueva_reserva = usuario1.crear_reserva(funcion_noche, asientos_usuario)

print(f"Reserva creada para: {usuario1.nombre}")
print(f"Monto original: ${nueva_reserva.monto_total}")
nueva_reserva.aplicar_promocion(promo_estudiante)
print(f"Monto con descuento: ${nueva_reserva.monto_total}")
nueva_reserva.confirmar_pago()

print("\nESTADO FINAL DE LA RESERVA")
print(f"Estado de la reserva: {nueva_reserva.estado.value}")

funcion_noche.calcular_asientos_dispo()

#los otros ejemplos se los pedi a una ia en base al que yo hice profe
#como le hacemos en clase, igual, le cambie unas cositas :D


#EJEMPLO 2
print("\n \n \nZONA DE COMIDA")
cine_snack = zonaComida(301, "dulceria", "planta baja", 300)

cine_snack.productos = {"palomitas": 30, "refrescos": 25, "nachos": 15}

usuario2 = usuario("Ana", "ana@mail", "222-9876")

print(f"Inventario inicial: {cine_snack.productos}")

print(f"{usuario2.nombre} compra")
cine_snack.vender_producto("palomitas", 3)

cine_snack.actualizar_stock("palomitas", 5)

print(f"Inventario final de productos: {cine_snack.productos}")

sala2 = sala(2, "Sala 2", "Planta 1", tipoSala.DOSD, 40)
peli2 = pelicula("Frozen", 110, "AA", "Animacion")
funcion2 = funcion(201, peli.titulo, sala2, 18, 120)

promo2 = promocion("FAM10", 0.10, "30.04.26")

print("\nESTADO INICIAL")
funcion2.calcular_asientos_dispo()

asientos = [1,2]
res = usuario2.crear_reserva(funcion2, asientos)

res.aplicar_promocion(promo2)
res.confirmar_pago()

print("ESTADO FINAL")
print(f"Estado reserva: {res.estado.value}")

funcion2.calcular_asientos_dispo()


#ejemplo 3
print("\n \n \nZONA DE COMIDA")
cine_snack = zonaComida(302, "dulceria", "planta baja", 400)

cine_snack.productos = {"palomitas": 40, "refrescos": 35, "nachos": 20}

usuario3 = usuario("Luis", "luis@mail", "222-8888")

print(f"{usuario3.nombre} compra")
cine_snack.vender_producto("refrescos", 4)

sala3 = sala(3, "Sala 3", "Planta 1", tipoSala.TRESD, 60)
peli3 = pelicula("Avatar", 190, "B", "Ciencia ficcion")
funcion3 = funcion(301, peli3.titulo, sala3, 20, 180)

asientos3 = [10,11,12]
res = usuario3.crear_reserva(funcion3, asientos3)

usuario3.cancelar_reserva(res)

print(f"Estado reserva: {res.estado.value}")



#ejemplo 4
print("\n \n \nZONA DE COMIDA")
cine_snack = zonaComida(303, "dulceria", "planta baja", 200)

cine_snack.productos = {"palomitas": 20, "refrescos": 20, "nachos": 10}

usuario4 = usuario("Carlos", "carlos@mail", "222-5555")
print(f"{usuario4.nombre} compra")

cine_snack.vender_producto("nachos", 1)

sala4 = sala(4, "Sala IMAX 2", "Planta 3", tipoSala.IMAX, 70)
peli4 = pelicula("Interstellar", 169, "B", "Ciencia ficcion")

funcion4 = funcion(401, peli4.titulo, sala4, 22, 200)

promo4 = promocion("SCI15", 0.15, "10.05.26")

asientos4 = [5,6]

res = usuario4.crear_reserva(funcion4, asientos4)

res.aplicar_promocion(promo4)
res.confirmar_pago()

print(f"estado reserva: {res.estado.value}")


#ejemplo 5
print("\n \n \nZONA DE COMIDA")

usuario5 = usuario("Sofia", "sofia@mail", "222-7777")

cine_snack = zonaComida(304, "dulceria", "planta 2", 500)

cine_snack.productos = {"palomitas": 50, "refrescos": 40, "nachos": 30}

print(f"{usuario5.nombre} compra")
cine_snack.vender_producto("palomitas", 5)

sala5 = sala(5, "Sala 5", "Planta 1", tipoSala.DOSD, 45)

peli5 = pelicula("Mario Bros", 95, "A", "Animacion")

funcion5 = funcion(501, peli5.titulo, sala5, 17, 100)

asientos5 = [3,4,5]

res = usuario5.crear_reserva(funcion5, asientos5)

print(f"estado reserva: {res.estado.value}")

#ejemplo 6
# sala
sala_vip = sala(6, "Sala VIP", "Planta 1", tipoSala.DOSD, 40)

# pelicula
peli6 = pelicula("Toy Story", 100, "AA", "Animación")

# función
funcion6 = funcion(106, peli6.titulo, sala_vip, 14, 120)

# usuario
usuario6 = usuario("Lucia", "lucia@mail", "222-8888")

# promoción
promo6 = promocion("INFANTIL", 0.15, "01.04.26")

print("\n \n \nESTADO INICIAL")
funcion6.calcular_asientos_dispo()

print("PROCESO DE RESERVA")

asientos_usuario = [5,6]
reserva6 = usuario6.crear_reserva(funcion6, asientos_usuario)

print(f"Reserva creada para: {usuario6.nombre}")
print(f"Monto original: ${reserva6.monto_total}")

reserva6.aplicar_promocion(promo6)
print(f"Monto con descuento: ${reserva6.monto_total}")

reserva6.confirmar_pago()
print(f"Estado de la reserva: {reserva6.estado.value}")

print("ESTADO FINAL")
funcion6.calcular_asientos_dispo()

#ejemplo7 

sala7 = sala(7, "Sala 2D Familiar", "Planta 1", tipoSala.DOSD, 60)

peli7 = pelicula("Frozen", 102, "A", "Animación")

funcion7 = funcion(107, peli7.titulo, sala7, 16, 110)

usuario7 = usuario("Pedro", "pedro@mail", "222-9999")

promo7 = promocion("FAMILIA", 0.20, "30.04.26")

print("\n \n \nESTADO INICIAL")
funcion7.calcular_asientos_dispo()

print("PROCESO DE RESERVA")

asientos_usuario = [8,9,10]
reserva7 = usuario7.crear_reserva(funcion7, asientos_usuario)

print(f"Reserva creada para: {usuario7.nombre}")
print(f"Monto original: ${reserva7.monto_total}")

reserva7.aplicar_promocion(promo7)
print(f"Monto con descuento: ${reserva7.monto_total}")

usuario7.cancelar_reserva(reserva7)

print("ESTADO FINAL")
print(reserva7.estado.value)


#ejemplo9

sala8 = sala(8, "Sala 3D Kids", "Planta 2", tipoSala.TRESD, 35)

peli8 = pelicula("Minions", 95, "A", "Comedia")

funcion8 = funcion(108, peli8.titulo, sala8, 12, 100)

usuario8 = usuario("Ana", "ana@mail", "222-7777")

promo8 = promocion("KIDS5", 0.05, "20.04.26")

print("\n \n \nESTADO INICIAL")
funcion8.calcular_asientos_dispo()

print("PROCESO DE RESERVA")

asientos_usuario = [1,2]
reserva8 = usuario8.crear_reserva(funcion8, asientos_usuario)

print(f"Reserva creada para: {usuario8.nombre}")
print(f"Monto original: ${reserva8.monto_total}")

reserva8.aplicar_promocion(promo8)
print(f"Monto con descuento: ${reserva8.monto_total}")

reserva8.confirmar_pago()
print(f"Estado de la reserva: {reserva8.estado.value}")

print("ESTADO FINAL")
funcion8.calcular_asientos_dispo()

#ejemplo 10

sala9 = sala(9, "Sala IMAX 3", "Planta 3", tipoSala.IMAX, 80)

peli9 = pelicula("Avatar", 190, "B", "Ciencia ficción")

funcion9 = funcion(109, peli9.titulo, sala9, 22, 180)

usuario9 = usuario("Sofia", "sofia@mail", "222-6666")

promo9 = promocion("IMAX15", 0.15, "15.05.26")

print("\n \n \nESTADO INICIAL")
funcion9.calcular_asientos_dispo()

print("PROCESO DE RESERVA")

asientos_usuario = [20,21,22,23]
reserva9 = usuario9.crear_reserva(funcion9, asientos_usuario)

print(f"Reserva creada para: {usuario9.nombre}")
print(f"Monto original: ${reserva9.monto_total}")

reserva9.aplicar_promocion(promo9)
print(f"Monto con descuento: ${reserva9.monto_total}")

print(f"Estado de la reserva: {reserva9.estado.value}")

print("ESTADO FINAL")
funcion9.calcular_asientos_dispo()