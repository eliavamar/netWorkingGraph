import numpy as np
import pandas as pd


class Csv:
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path, index_col=0)

    def get_df(self):
        return self.df

    def get_columns(self) -> list:
        return self.df.columns.values.tolist()

    def group_by(self, columns: list, agg_functions: list):
        return self.df.groupby(columns).agg(agg_functions)

    def get_arr_for_predict_by_columns(self, columns: list):
        return np.array([np.array([self.df[column][int(i)] for column in columns]) for i in range(1, len(self.df))])

    def result_to_csv(self, cls_predict, path_for_new_file="output.cvs"):
        pd.DataFrame(cls_predict).to_csv(path_for_new_file)
