import pandas as pd


def minuscula(df):
    """Convierte a minúsculas las columnas de tipo object"""
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()


def comas(df):
    """Remplaza comas por puntos y convierte a float las columnas que se puedan convertir"""
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(",", ".")
        try:
            df[col] = df[col].astype("float64")
        except:
            pass


def espacios(df):
    """Remplaza espacios por guiones bajos en los valores de las columnas de tipo object"""
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(" ", "_")



