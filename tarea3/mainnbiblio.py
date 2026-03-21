from jjjj import *

libro1= Libro(123, "cuentos", 2023, True, "May", 13, "fantasia")
libro2 = Libro(124, "El Aleph", 1945, True, "Jorge Luis Borges", 14, "Ficción")
libro3 = Libro(125, "Rayuela", 1963, True, "Julio Cortázar", 15, "Novela")
libro4 = Libro(126, "Solaris", 1961, False, "Stanisław Lem", 16, "Ciencia Ficción")
libro5 = Libro(127, "Drácula", 1897, True, "Bram Stoker", 17, "Terror")
libro6 = Libro(128, "Fundación", 1951, True, "Isaac Asimov", 18, "Sci-Fi")
libro7 = Libro(129, "El Tunel", 1948, False, "Ernesto Sabato", 19, "Psicológico")
libro8 = Libro(130, "Metamorfosis", 1915, True, "Franz Kafka", 20, "Absurdo")
libro9 = Libro(131, "1984", 1949, True, "George Orwell", 21, "Distopía")
libro10 = Libro(132, "Frankenstein", 1818, True, "Mary Shelley", 22, "Gótico")


revista1= Revista(234, "cocina", 2024, True, 2, "mensual")
revista2 = Revista(235, "Muy Interesante", 2024, True, 5, "Mensual")
revista3 = Revista(236, "Vogue", 2023, True, 12, "Mensual")
revista4 = Revista(237, "Time", 2024, False, 45, "Semanal")
revista5 = Revista(238, "Rolling Stone", 2024, True, 8, "Mensual")
revista6 = Revista(239, "Forbes", 2023, True, 110, "Bimensual")
revista7 = Revista(240, "Nature", 2024, True, 300, "Semanal")
revista8 = Revista(241, "National Geographic", 2024, False, 15, "Mensual")
revista9 = Revista(242, "PC World", 2022, True, 50, "Trimestral")
revista10 = Revista(243, "Architectural Digest", 2024, True, 4, "Mensual")



digital1=MaterialDigital(345, "leyendas", 2018, False, "PDF", "https://dcshuhk", 34)
digital2 = MaterialDigital(346, "Deep Learning", 2022, True, "PDF", "https://bit.ly/dl-guide", 45)
digital3 = MaterialDigital(347, "React Basics", 2023, True, "EPUB", "https://learn.dev/react", 12)
digital4 = MaterialDigital(348, "SQL Pro", 2021, False, "MOBI", "https://db-docs.com/sql", 8)
digital5 = MaterialDigital(349, "Cybersecurity", 2024, True, "PDF", "https://sec.org/intro", 56)
digital6 = MaterialDigital(350, "UI Design", 2023, True, "PDF", "https://design.io/ui", 22)
digital7 = MaterialDigital(351, "Agile Docs", 2020, True, "DOCX", "https://agile.com/manifesto", 5)
digital8 = MaterialDigital(352, "Rust Lang", 2024, False, "PDF", "https://rust-lang.org/book", 30)
digital9 = MaterialDigital(353, "Data Science", 2023, True, "PDF", "https://ds-hub.com/intro", 67)
digital10 = MaterialDigital(354, "Docker 101", 2022, True, "PDF", "https://docker.com/get-started", 18)



per1=Persona("Caro")
per2 = Persona("Mateo")
per3 = Persona("Sofia")
per4 = Persona("Lucas")
per5 = Persona("Valentina")
per6 = Persona("Julian")
per7 = Persona("Camila")
per8 = Persona("Nicolas")
per9 = Persona("Elena")
per10 = Persona("Sebastian")

usu1=Usuario("Daniel", 4)
usu2 = Usuario("Mariana", 3)
usu3 = Usuario("Roberto", 5)
usu4 = Usuario("Lucia", 2)
usu5 = Usuario("Fernando", 6)
usu6 = Usuario("Gabriela", 4)
usu7 = Usuario("Esteban", 1)
usu8 = Usuario("Paola", 5)
usu9 = Usuario("Ricardo", 3)
usu10 = Usuario("Jimena", 2)


biblio=Bibliotecario("may")
biblio2=Bibliotecario("dani")

usu1.revisarpuede_prestamo()

sucu1=Sucursal(123, "central")
sucu2=Sucursal(234, "norte")

sucu1.catalogoLocal.append(libro1)
sucu1.catalogoLocal.append(libro4)
sucu1.catalogoLocal.append(libro5)
sucu1.catalogoLocal.append(revista1)
sucu1.catalogoLocal.append(revista10)
sucu1.catalogoLocal.append(revista6)
sucu1.catalogoLocal.append(revista8)
sucu1.catalogoLocal.append(digital7)
sucu1.catalogoLocal.append(digital3)
sucu1.catalogoLocal.append(digital2)

sucu2.catalogoLocal.append(digital1)
sucu2.catalogoLocal.append(libro1)
sucu2.catalogoLocal.append(libro2)
sucu2.catalogoLocal.append(libro5)
sucu2.catalogoLocal.append(revista1)
sucu2.catalogoLocal.append(revista5)
sucu2.catalogoLocal.append(revista6)
sucu2.catalogoLocal.append(revista8)
sucu2.catalogoLocal.append(digital7)
sucu2.catalogoLocal.append(digital10)
sucu2.catalogoLocal.append(digital2)


presta1=Prestamo(123, date(26, 3, 10), date(26, 3, 25), usu1, libro1)
presta2=Prestamo(234, date(26, 3, 8), date(26, 3, 23), usu1, revista5)
presta3=Prestamo(345, date(26, 3, 4), date(26, 3, 19), usu1, libro2)
presta4=Prestamo(456, date(26, 3, 10), date(26, 3, 25), usu1, libro3)


usu1.listaActiva.append(presta1)
biblio.gestionar_prestamo(presta1)
biblio.transferir_material(libro1, sucu1, sucu2)

pena1=Penalizacion(0, "no entrego a tiempo", True)
pena1.calcular_multa(3)

pena2=Penalizacion(0, "no entrego a tiempo", False)
pena2.bloquear_usuario("Daniel")

catalogo=Catalogo()
catalogo.agregar_materiales(libro1)
catalogo.agregar_materiales(revista5)
catalogo.agregar_materiales(digital10)

catalogo.buscar_por_autor("May")

catalogo.buscar_todas_sucursales("cuentos", [sucu1, sucu2])