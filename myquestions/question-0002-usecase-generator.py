import pandas as pd
import numpy as np
import random


def generar_caso_de_uso_clasificar_base_lubricante():
    n_muestras = random.randint(5, 15)
    vi = []
    fp = []
    pp = []
    expected = []

    for _ in range(n_muestras):
        tipo = random.choice(['Sintético', 'Mineral'])
        if tipo == 'Sintético':
            v = random.randint(151, 180)
            f = random.randint(231, 260)
            p = random.randint(-60, -40)
        else:
            v = random.randint(100, 149)
            f = random.randint(190, 225)
            p = random.randint(-30, -10)

        vi.append(v)
        fp.append(f)
        pp.append(p)
        expected.append('Sintético' if v > 150 and f > 230 else 'Mineral')

    input_data = {'muestras': pd.DataFrame({'viscosity_index': vi, 'flash_point': fp, 'pour_point': pp})}
    return input_data, expected