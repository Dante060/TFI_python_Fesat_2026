from funciones_sensores import limpiar_registro_sensor
from funciones_sensores import generar_resumen_sensores
if __name__ == "__main__":
    datos_sensores_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "sensor-002", "temperatura": "31.2°C", "ubicacion": "  Planta Sur "},
    {"sensor_id": " SENSOR-003  ", "temperatura": "19.8", "ubicacion": "Planta Este"},
    {"sensor_id": "SENSOR-004", "temperatura": "28.0 C", "ubicacion": "Planta Oeste"},
    {"sensor_id": "  ", "temperatura": "N/A", "ubicacion": "Desconocido"}] # Un caso extremo por si acaso

print("--- Datos Procesados de Sensores---")
sensores_limpios = [limpiar_registro_sensor(reg) for reg in datos_sensores_crudos]

for m in sensores_limpios:
    print (m)

print("\n --- Reporte Final ---")
alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral_temperatura= 25.0)
print(f"sensores en Alerta > 25.0°C: {alertas}")
print(f"Promedio de Temperatura Censada: {promedio}°C")