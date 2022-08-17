from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest

from utils import get_default_dbscan_params, get_default_isolation_forest_params


def dbscan(arr, params=get_default_dbscan_params()):
    cls = DBSCAN()

    cls.min_samples = params["min_samples"]
    cls.eps = params["eps"]
    cls.metric = params["metric"]
    cls.metric_params = params["metric_params"]
    cls.algorithm = params["algorithm"]
    cls.leaf_size = params["leaf_size"]
    cls.p = params["p"]
    cls.n_jobs = params["n_jobs"]

    return cls.fit_predict(arr)


def isolation_forest(arr, params=get_default_isolation_forest_params()):
    cls = IsolationForest()

    cls.n_estimators = params["n_estimators"]
    cls.max_samples = params["max_samples"]
    cls.contamination = params["contamination"]
    cls.max_features = params["max_features"]
    cls.bootstrap = params["bootstrap"]
    cls.n_jobs = params["n_jobs"]
    cls.random_state = params["random_state"]
    cls.verbose = params["verbose"]
    cls.warm_start = params["warm_start"]
    print(arr)
    return cls.fit_predict(arr)
