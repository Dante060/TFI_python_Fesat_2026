def calcular_emisiones_carbono(consumo_kwh, factor_emision = 0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no  puede ser negativo")
    return (consumo_kwh * factor_emision)

def obtener_metricas_consumo(registros):
    if not registros:
        return {"total_emisiones_global":0, "planta_mayor_consumo": "Ninguna"}

    total_emisiones_global = 0
    max_consumo = -1
    planta_mayor_consumo = ""

    for reg in registros:
        consumo = reg["consumo"]
        planta = reg["planta"]
        total_emisiones_global += calcular_emisiones_carbono(consumo)
        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor_consumo = planta

    return {
        "total_emisiones_global": total_emisiones_global,
        "planta_mayor_consumo": planta_mayor_consumo
    }