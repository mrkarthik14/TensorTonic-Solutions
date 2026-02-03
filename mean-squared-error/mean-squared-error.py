import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.asarray(y_pred).ravel()
    y_true = np.asarray(y_true).ravel()

    if y_pred.shape != y_true.shape:
        return None

    error = y_pred - y_true
    square = error ** 2
    mse = np.mean(square)
    return float(mse)
    pass
