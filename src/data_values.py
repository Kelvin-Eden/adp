import pandas as pd


class Dataset:
    def __init__(self, path):
        self.path = path

    def read(self):
        return pd.read_csv(self.path).dropna(axis=1)

    @property
    def criteria(self):
        data = self.read()
        x = data.iloc[:, :-1]
        return [" ".join([i.capitalize() for i in value.split("_")]) for value in x.columns.values]

    @property
    def diseases(self):
        data = self.read()
        return data['prognosis'].value_counts().index.to_list()


