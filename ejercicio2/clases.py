from excepciones import StockInvalidoError
import json

class DispositivoEcologico:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError(f"Error en {self.nombre} : no se puede asignar un valor negativo, {nuevo_stock} al stock")
        self._stock = nuevo_stock

    def generar_ficha_tecnica(self):
        return {"id_producto":self.id_producto, "nombre":self.nombre, "precio":f"${self.precio:.2f}", "stock":self._stock}

class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha_tecnica = super().generar_ficha_tecnica()
        ficha_tecnica.update({"eficiencia":f"{self.eficiencia}%", "potencia": f"{self.potencia_w}W"})
        return ficha_tecnica

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializar = [dispositivo.generar_ficha_tecnica() for dispositivo in lista_dispositivos]

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializar, archivo, indent=4,ensure_ascii=False)
            