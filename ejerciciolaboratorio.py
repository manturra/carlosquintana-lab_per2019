class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_info(self):
        return [self.nombre, self.precio]

class Medicamento(Producto):
    def __init__(self, nombre, precio, compuesto, porcentaje):
        super().__init__(nombre, precio)
        self.compuesto = compuesto
        self.porcentaje = porcentaje
    def get_info(self):
        return [self.nombre, self.precio, self.compuesto, self.porcentaje]

class Laboratorio():
    def __init__(self, nombre, lista_productos):
        self.nombre = nombre
        self.lista_productos = lista_productos
    def info_lab(self):
        lista_info_lab = []
        for i in range(len(lista_productos)):
            lista_info_lab.append(lista_productos[i].get_info())
        return lista_info_lab

producto1 = Producto("Crema solar", 40)
producto2 = Medicamento("Ibuprofeno", 5, "lactosa", 0.5)
producto3 = Producto("Cepillos de dientes", 3)
lista_productos = []
lista_productos.append(producto1)
lista_productos.append(producto2)
lista_productos.append(producto3)
laboratorio1 = Laboratorio("Medialab", lista_productos)
print("El laboratorio tiene", laboratorio1.info_lab())
