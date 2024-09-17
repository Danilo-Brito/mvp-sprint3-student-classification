import pandas as pd


class Charger:

    def charge_data(url: str, attributes: list):
        # Carrega os dados e retorna um DataFrame.

        return pd.read_csv(url, names=attributes, header=0)
