

import pandas as pd

def eda_preliminar (df):

    """
    Realiza un análisis exploratorio preliminar de un DataFrame de pandas
    este analisis incluye:
    - Muestra 5 filas aleatorias del DataFrame
    -informacion general del dataframe (tipo de datos, nulos, etc)
    - porcentaje de valores nulos por columnas
    - distribucion de valores para columnas categoricas

    parametros:
    df: pd.DataFrame
        DataFrame a analizar
    returns:
    None
    """



    display(df.sample(5))


    print ("-------------------------------")
    print ("DIMENSIONES DEL DATAFRAME")
    print(f'nuestro conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas')

    print ("-------------------------------")
    print ("INFO")
    display(df.info())

    print ("-------------------------------")
    print ("NULOS")
    display(df.isnull().mean()*100)

    print ("-------------------------------")
    print ("DUPLICADOS")
    print (f"tenemos un total de  {df.duplicated().sum()} duplicados")

    print ("-------------------------------")
    print ("FRECUENCIA CATEGORICAS")
    for col in df.select_dtypes(include='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('-'*10)

    print ("-------------------------------")
    print ("ESTADISTICAS NUMERICAS")
    display(df.describe().T)