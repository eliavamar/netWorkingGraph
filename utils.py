def agg_function_list() -> list:
    return ["count", "size", "sum", "mean", "average", "std", "var", "sem", "describe", "min", "max", "first", "last"]


def get_default_dbscan_params() -> dict:
    return {
        "eps": 0.5,
        "min_samples": 5,
        "metric": "euclidean",
        "metric_params": None,
        "algorithm": "auto",
        "leaf_size": 30,
        "p": None,
        "n_jobs": None
    }


def get_default_isolation_forest_params() -> dict:
    return {
        "n_estimators": 100,
        "max_samples": "auto",
        "contamination": "auto",
        "max_features": 1.0,
        "bootstrap": False,
        "n_jobs": None,
        "random_state": None,
        "verbose": 0,
        "warm_start": False
    }
