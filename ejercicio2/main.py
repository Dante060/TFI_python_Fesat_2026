import os
from excepciones import StockInvalidoError
from clases import DispositivoEcologico, PanelSolar, GestorInventario

if __name__ == "__main__":
    # 1. Preparamos la ruta exacta dentro de la carpeta ejercicio2
    carpeta_ejercicio2 = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_ejercicio2, "catalogo_ecotech.json")

    # 2. Inicializamos la lista y creamos los productos válidos
    catalogo_valido = []

    disp_base = DispositivoEcologico("ECO-001", "Termostato Inteligente", 120.50, 15)
    panel_1 = PanelSolar("SOL-101", "Panel Monocristalino Pro", 450.00, 8, 22.5, 550)
    
    catalogo_valido.append(disp_base)
    catalogo_valido.append(panel_1)

    # 3. Pruebas controladas de StockInvalidoError
    print("--- Iniciando prueba de validación de inventario ---")
    try:
        panel_fallido = PanelSolar("SOL-999", "Panel Defectuoso", 300.00, -5, 18.0, 400)
        catalogo_valido.append(panel_fallido)
    except StockInvalidoError as error:
        print(f"[EXCEPCIÓN CAPTURADA EXITOSAMENTE]: {error}")

    try:
        disp_base.stock = -10
    except StockInvalidoError as error:
        print(f"[EXCEPCIÓN CAPTURADA EXITOSAMENTE]: {error}")

    # 4. Guardamos al final usando la ruta_json que apunta a ejercicio2
    GestorInventario.guardar_catalogo_json(catalogo_valido, ruta_json)
    print(f"\nCatálogo exportado exitosamente a '{ruta_json}' con {len(catalogo_valido)} productos válidos.")
