import pytest
import json
from excepciones import StockInvalidoError
from clases import DispositivoEcologico, PanelSolar, GestorInventario

# --- Fixtures: Preparan los objetos limpios antes de cada test ---
@pytest.fixture
def dispositivo_base():
    return DispositivoEcologico("ECO-01", "Sensor Agua", 100.0, 10)

@pytest.fixture
def panel_solar():
    return PanelSolar("SOL-01", "Panel 500W", 500.0, 5, 21.5, 500)

# --- 1. Prueba de Encapsulamiento y Validación de Stock ---
def test_stock_valido(dispositivo_base):
    dispositivo_base.stock = 0  # El 0 debe ser permitido
    assert dispositivo_base.stock == 0
    
    dispositivo_base.stock = 25
    assert dispositivo_base.stock == 25

# --- 2. Prueba de Excepción Personalizada ---
def test_stock_negativo_al_instanciar():
    with pytest.raises(StockInvalidoError):
        DispositivoEcologico("ECO-99", "Falla", 50.0, -1)

def test_stock_negativo_al_modificar(dispositivo_base):
    with pytest.raises(StockInvalidoError) as info_error:
        dispositivo_base.stock = -5
    # También verificamos que el mensaje dinámico incluya el nombre del producto
    assert "Sensor Agua" in str(info_error.value)

# --- 3. Prueba de Herencia y Polimorfismo ---
def test_ficha_tecnica_base(dispositivo_base):
    ficha = dispositivo_base.generar_ficha_tecnica()
    assert isinstance(ficha, dict)
    assert ficha["precio"] == "$100.00"
    assert "eficiencia" not in ficha

def test_ficha_tecnica_polimorfismo_panel(panel_solar):
    ficha = panel_solar.generar_ficha_tecnica()
    assert ficha["precio"] == "$500.00"
    assert ficha["eficiencia"] == "21.5%"
    assert ficha["potencia"] == "500W"

# --- 4. Prueba de Persistencia en JSON ---
def test_guardar_catalogo_json(dispositivo_base, panel_solar, tmp_path):
    # tmp_path es una carpeta temporal automática que pytest crea y limpia solo
    ruta_temporal = tmp_path / "test_catalogo.json"
    lista = [dispositivo_base, panel_solar]
    
    GestorInventario.guardar_catalogo_json(lista, ruta_temporal)
    
    assert ruta_temporal.exists()
    
    datos_leidos = json.loads(ruta_temporal.read_text(encoding="utf-8"))
    assert len(datos_leidos) == 2
    assert datos_leidos[0]["id_producto"] == "ECO-01"
    assert datos_leidos[1]["potencia"] == "500W"
