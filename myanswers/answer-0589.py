import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.covariance import EllipticEnvelope

def conteo_anomalias_elipticas(df, contaminacion):
    imputer = SimpleImputer(strategy='mean')
    df_imputado = imputer.fit_transform(df)
    modelo = EllipticEnvelope(contamination=contaminacion, random_state=42)
    modelo.fit(df_imputado)
    predicciones = modelo.predict(df_imputado)
    return int(np.sum(predicciones == -1))
