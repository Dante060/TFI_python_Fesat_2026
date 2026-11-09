def limpiar_registro_sensor(registro_raw):
    registro_limpio = {}
    sensor_id_raw = registro_raw.get("sensor_id","")
    registro_limpio["sensor_id"] = sensor_id_raw.strip()

    temperatura_raw = registro_raw.get("temperatura","0")
    temperatura_limpio = temperatura_raw.replace("C", "").replace("F","").replace("°","").strip()
    try:
        registro_limpio["temperatura"] = float(temperatura_limpio)
    except ValueError:
        registro_limpio["temperatura"] = 0.0

    ubicacion_raw = registro_raw.get("ubicacion","")
    if ubicacion_raw is None or str(ubicacion_raw).strip() == "": #si zona_raw esta vacio o al limpiarlo queda vacio, va a guardar en el diccionario en zona "General"
        registro_limpio["ubicacion"] = "Área No Asignada"
    else:
        registro_limpio["ubicacion"] = str(ubicacion_raw).strip()

    return registro_limpio

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    if lista_sensores_limpios == []:
        return [] , 0.0
    
    acumulador_total = 0.0
    lista_sensores_alerta = []

    for temp in lista_sensores_limpios:
        temp_sensor = temp["temperatura"]
        if temp_sensor > umbral_temperatura:
            lista_sensores_alerta.append(temp["sensor_id"])
        acumulador_total += temp_sensor

    promedio_temperatura = round((acumulador_total / len(lista_sensores_limpios)),2)
    return lista_sensores_alerta, promedio_temperatura