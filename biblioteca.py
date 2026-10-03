#BIBLIOTECA
# Implementacion de encapsulamiento, property y constructores
# Clase Libro. para representar un libro en la biblioteca
class Libro:

    def __init__(self, titulo, autor, id, cantidad_ejemplares=1,
                 *etiquetas, categoria="General", **datos_adicionales):

        # Atributos publicos
        self.titulo = titulo
        self.autor = autor
        self.id = id

        # Atributo protegido
        self._ejemplares_totales = cantidad_ejemplares

        # Atributo privado
        self.__ejemplares_disponibles = cantidad_ejemplares

        # Argumentos variables
        self.etiquetas = etiquetas
        self.categoria = categoria
        self.datos_adicionales = datos_adicionales

    # GETTER: consultar ejemplares totales
    @property
    def ejemplares_totales(self):
        return self._ejemplares_totales

    # SETTER: modificar ejemplares totales
    @ejemplares_totales.setter
    def ejemplares_totales(self, cantidad):

        if cantidad < self.__ejemplares_disponibles:
            raise ValueError("No puede haber menos ejemplares totales que disponibles")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        self._ejemplares_totales = cantidad

    # GETTER: consultar ejemplares disponibles
    @property
    def ejemplares_disponibles(self):
        return self.__ejemplares_disponibles

    # SETTER: modificar ejemplares disponibles
    @ejemplares_disponibles.setter
    def ejemplares_disponibles(self, cantidad):

        if cantidad < 0 or cantidad > self._ejemplares_totales:
            raise ValueError("Cantidad de ejemplares no valida")

        self.__ejemplares_disponibles = cantidad

    # Metodo para registrar el prestamo de un libro
    def registrar_prestamo(self):

        if self.ejemplares_disponibles <= 0:
            raise ValueError("No hay ejemplares disponibles")

        self.ejemplares_disponibles -= 1

    # Metodo para registrar la devolucion de un libro
    def registrar_devolucion(self):

        if self.ejemplares_disponibles >= self.ejemplares_totales:
            raise ValueError("Todos los ejemplares ya estan disponibles")

        self.ejemplares_disponibles += 1


# Clase Estudiante. representa a un estudiante que puede tomar prestado libros de la biblioteca
class Estudiante:

    def __init__(self, nombre, codigo, carrera="Sin asignar",
                 *cursos, activo=True, **datos_adicionales):

        # Atributo publico
        self.nombre = nombre

        # Atributo privado
        self.__codigo = codigo

        # Atributo protegido
        self._carrera = carrera

        # Valores adicionales
        self.cursos = cursos
        self.activo = activo
        self.datos_adicionales = datos_adicionales

    # GETTER: consultar codigo del estudiante
    @property
    def codigo(self):
        return self.__codigo

    # GETTER: consultar carrera
    @property
    def carrera(self):
        return self._carrera

    # SETTER: modificar carrera
    @carrera.setter
    def carrera(self, nueva_carrera):

        if not nueva_carrera:
            raise ValueError("La carrera no puede estar vacia")

        self._carrera = nueva_carrera


# Clase Bibliotecario. representa a un usuario que administra la biblioteca
class Bibliotecario:

    def __init__(self, nombre, identificacion, horario="No asignado",
                 cargo="Bibliotecario", **datos_adicionales):

        # Atributo publico
        self.nombre = nombre

        # Atributo privado
        self.__identificacion = identificacion

        # Atributo protegido
        self._horario = horario

        self.cargo = cargo
        self.datos_adicionales = datos_adicionales

    # GETTER: consultar identificacion
    @property
    def identificacion(self):
        return self.__identificacion

    # GETTER: consultar horario
    @property
    def horario(self):
        return self._horario

    # SETTER: modificar horario
    @horario.setter
    def horario(self, nuevo_horario):

        if not nuevo_horario:
            raise ValueError("El horario no puede estar vacio")

        self._horario = nuevo_horario


# Clase Prestamo. para representar un préstamo de un libro a un estudiante
class Prestamo:

    def __init__(self, libro, estudiante, id_prestamo,
                 fecha_prestamo, fecha_devolucion=None,
                 *observaciones, estado="Activo", **datos_adicionales):

        # Atributos publicos
        self.libro = libro
        self.estudiante = estudiante
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo

        # Atributo protegido
        self._fecha_devolucion = fecha_devolucion

        # Atributo privado
        self.__estado = estado

        # Argumentos adicionales
        self.observaciones = observaciones
        self.datos_adicionales = datos_adicionales

        # Registrar automaticamente el prestamo del libro
        if self.__estado == "Activo":
            self.libro.registrar_prestamo()

    # GETTER: consultar fecha de devolucion
    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    # SETTER: modificar fecha de devolucion
    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha):

        if not nueva_fecha:
            raise ValueError("Debe ingresar una fecha de devolucion")

        self._fecha_devolucion = nueva_fecha

    # GETTER: consultar estado del prestamo
    @property
    def estado(self):
        return self.__estado

    # Metodo para devolver el libro
    def devolver(self, fecha_devolucion):

        if self.__estado != "Activo":
            raise ValueError("Este prestamo ya fue devuelto")

        if not fecha_devolucion:
            raise ValueError("Debe ingresar la fecha de devolucion")

        self.libro.registrar_devolucion()

        self._fecha_devolucion = fecha_devolucion
        self.__estado = "Devuelto"


# Creación de objetos
libro_1 = Libro(
    "Piensa en Python",
    "Allen B. Downey",
    "102-20260920",
    3,
    "Programacion",
    "Educativo",
    categoria="Ingenieria"
)

estudiante_1 = Estudiante(
    "Breiner Pabon",
    "12345",
    "Ingenieria de Sistemas"
)

bibliotecario_1 = Bibliotecario(
    "Maria Gomez",
    "B01",
    "08:00-17:00",
    "Bibliotecario"
)

prestamo_1 = Prestamo(
    libro_1,
    estudiante_1,
    "P01",
    "20/09/2026",
    "02/10/2026"
)


# Mostrar información de los objetos
print("\n----- INFORMACION DEL LIBRO -----")

print("Titulo:", libro_1.titulo)
print("Autor:", libro_1.autor)
print("Codigo:", libro_1.id)
print("Categoria:", libro_1.categoria)
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

print("ID:", prestamo_1.id_prestamo)
print("Libro:", prestamo_1.libro.titulo)
print("Estudiante:", prestamo_1.estudiante.nombre)
print("Fecha de prestamo:", prestamo_1.fecha_prestamo)
print("Fecha de devolucion:", prestamo_1.fecha_devolucion)
print("Estado:", prestamo_1.estado)

