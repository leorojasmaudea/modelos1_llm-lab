import pandas as pd
import random


def generar_caso_de_uso_normalizar_datos_legados():
    n = random.randint(5, 10)
    fechas = [f"202{random.randint(0, 5)}{random.randint(1, 12):02d}{random.randint(1, 28):02d}" for _ in range(n)]
    codigos = [random.randint(1, 4) for _ in range(n)]

    df_input = pd.DataFrame({'fecha_raw': fechas, 'cod_estado': codigos})

    # Calcular esperado
    df_expected = df_input.copy()
    df_expected['fecha_raw'] = pd.to_datetime(df_expected['fecha_raw'], format='%Y%m%d')
    mapping = {1: 'Activo', 2: 'Inactivo', 3: 'Pendiente'}
    df_expected['estado_desc'] = df_expected['cod_estado'].map(lambda x: mapping.get(x, 'Error'))
    df_expected = df_expected.drop(columns=['cod_estado'])

    return {'registros': df_input}, df_expected