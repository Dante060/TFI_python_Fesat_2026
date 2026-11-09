from django.shortcuts import render
from utils import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    registros_consumo = [
        {"planta": "Planta A", "consumo": 150},
        {"planta": "Planta B", "consumo": 200},
        {"planta": "Planta C", "consumo": 50},
        {"planta": "Planta D", "consumo": 300},
        {"planta": "Planta E", "consumo": 0},
        {"planta": "Planta F", "consumo": 20}  # Este registro tiene un consumo negativo para probar la validación
    ]

    metricas = obtener_metricas_consumo(registros_consumo)

    return render(request, "sustentabilidad/panel.html",metricas)