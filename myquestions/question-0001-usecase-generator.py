import pandas as pd
import numpy as np
import random


def generar_caso_de_uso_clasificar_movimiento_rfid():
    """
    Genera un caso de uso aleatorio para la clasificación de movimiento RFID.
    Retorna: (input_dict, expected_output)
    """
    # Decidir aleatoriamente si el caso será estático o en movimiento
    es_movimiento = random.choice([True, False])
    n_lecturas = random.randint(15, 40)

    if es_movimiento:
        # Alta varianza en RSSI y cambios en fase
        rssi = np.random.normal(loc=-60, scale=4.0, size=n_lecturas)
        phase = np.random.uniform(0, 1.0, size=n_lecturas)
        expected_output = "Moving"
    else:
        # Baja varianza (señal estable)
        rssi = np.random.normal(loc=-55, scale=1.0, size=n_lecturas)
        phase = np.random.normal(loc=0.2, scale=0.05, size=n_lecturas)
        expected_output = "Static"

        # Caso borde: Forzar Static si por azar la varianza fuera alta (poco probable)
        if np.var(rssi) > 8.0 or (np.max(phase) - np.min(phase)) > 0.5:
            expected_output = "Moving"

    # Crear el DataFrame y el diccionario de entrada
    df_lecturas = pd.DataFrame({
        'rssi': rssi.tolist(),
        'phase': phase.tolist()
    })

    input_dict = {'lecturas': df_lecturas}

    return input_dict, expected_output


# Ejemplo de ejecución local para validación
if __name__ == "__main__":
    inputs, output = generar_caso_de_uso_clasificar_movimiento_rfid()
    print(f"Input (primeras 5 filas): \n{inputs['lecturas'].head()}")
    print(f"Output esperado: {output}")