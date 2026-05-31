from sklearn.preprocessing import StandardScaler, MinMaxScaler

def escalar_datos_concreto(df):
    scaler_std = StandardScaler()
    data_std = scaler_std.fit_transform(df)
    scaler_minmax = MinMaxScaler()
    return scaler_minmax.fit_transform(data_std)
