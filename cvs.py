import pandas as pd


class Cvs:

    # TODO: remove index col from cvs file in __init__ function
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)

    def get_columns(self) -> list:
        return self.df.columns.values.tolist()

    # TODO: fix group_by function
    def group_by(self, columns: list, agg_function):
        return self.df.groupby(columns).agg[agg_function]()

    def get_new_df_by_columns(self, columns: list):
        return self.df.filter(columns, axis=1)
