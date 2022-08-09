from sklearn.cluster import DBSCAN
import pandas as pd

# TODO: check insert dynamic params
@staticmethod
def dbscan(df, path_for_new_file="output.cvs"):
    pd.DataFrame(DBSCAN(min_samples=200).fit_predict(df)).to_csv(path_for_new_file)
