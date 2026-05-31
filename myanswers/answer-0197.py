import pandas as pd

def resumen_ventas_por_categoria(df):
    df_calc = df.copy()
    df_calc['ingreso_total'] = df_calc['precio_unitario'] * df_calc['cantidad_vendida']
    resumen = df_calc.groupby('categoria').agg(
        total_ingresos=('ingreso_total', 'sum'),
        total_unidades=('cantidad_vendida', 'sum'),
        precio_promedio=('precio_unitario', 'mean')
    ).reset_index()
    return resumen
