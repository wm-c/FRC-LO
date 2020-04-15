import pandas as pd

data = pd.read_excel("Data.xlsx")


def getRow(row: int) -> pd.core.series.Series:
    return data.iloc[row]

def getSize() -> int:
    return data.index.stop






