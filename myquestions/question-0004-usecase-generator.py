import pandas as pd
import random


def generar_caso_de_uso_detectar_ocupacion_fantasma():
    celdas = list(range(100, 120))
    # Sensores: algunos ocupados (1), otros libres (0)
    estados = [random.choice([0, 1]) for _ in celdas]
    df_sensores = pd.DataFrame({'celda_id': celdas, 'estado_sensor': estados})

    # Celdas que realmente están pagadas (solo de las que el sensor marcó como 1)
    ocupadas = [c for c, e in zip(celdas, estados) if e == 1]
    # Simulamos que algunas de esas ocupadas no tienen pago (fantasmas)
    pagadas = random.sample(ocupadas, k=len(ocupadas) // 2) if ocupadas else []
    df_pagos = pd.DataFrame({'celda_id': pagadas})

    # Resultado esperado
    fantasmas = sorted([c for c in ocupadas if c not in pagadas])

    input_data = {'sensor_data': df_sensores, 'pagos_activos': df_pagos}
    return input_data, fantasmas