# Clase Libro. para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, id, cantidad_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.ejemplares_totales = cantidad_ejemplares
        self.ejemplares_disponibles = cantidad_ejemplares


# Clase Estudiante. representa a un estudiante que puede tomar prestado libros de la biblioteca
class Estudiante:
    def __init__(self, nombre, codigo, carrera):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera


# Clase Bibliotecario. representa a un usuario que administra la biblioteca
class Bibliotecario:
    def __init__(self, nombre, identificacion, horario, cargo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.horario = horario
        self.cargo = cargo


# Clase Prestamo. para representar un préstamo de un libro a un estudiante
class Prestamo:
    def __init__(self, libro, estudiante, id_estudiante, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.estudiante = estudiante
        self.id_estudiante = id_estudiante
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion


# Creación de objetos

libro_1 = Libro("Piensa en Python","Allen B. Downey","102-20260920",3)

estudiante_1 = Estudiante("Breiner Pabon","12345","Ingenieria de Sistemas")

bibliotecario_1 = Bibliotecario("Maria Gomez","B01","08:00-17:00","Bibliotecario")

prestamo_1 = Prestamo(libro_1,estudiante_1,"P01","20/09/2026","02/10/2026")


# Mostrar información de los objetos

print("----- INFORMACION DEL LIBRO -----")
print("Titulo:", libro_1.titulo)
print("Autor:", libro_1.autor)
print("Codigo:", libro_1.id)
print("Ejemplares totales:", libro_1.ejemplares_totales)
print("Ejemplares disponibles:", libro_1.ejemplares_disponibles)

print("\n----- INFORMACION DEL ESTUDIANTE -----")
print("Nombre:", estudiante_1.nombre)
print("Codigo:", estudiante_1.codigo)
print("Carrera:", estudiante_1.carrera)

print("\n----- INFORMACION DEL BIBLIOTECARIO -----")
print("Nombre:", bibliotecario_1.nombre)
print("Identificacion:", bibliotecario_1.identificacion)
print("Horario:", bibliotecario_1.horario)
print("Cargo:", bibliotecario_1.cargo)

print("\n----- INFORMACION DEL PRESTAMO -----")
print("ID:", prestamo_1.id_estudiante)
print("Libro:", prestamo_1.libro.titulo)
print("Estudiante:", prestamo_1.estudiante.nombre)
print("Fecha de prestamo:", prestamo_1.fecha_prestamo)
print("Fecha de devolucion:", prestamo_1.fecha_devolucion)