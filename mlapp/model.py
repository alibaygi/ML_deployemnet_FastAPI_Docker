import pickle
from pathlib import Path
import numpy as np


__version__ = "0.1.0"

BASE_DIR = Path().resolve(strict=True)


# with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
#     model = pickle.load(f)

with open(f"./trained_pipeline-0.1.0.pkl", "rb") as f:
    model = pickle.load(f)


def predict_pipeline(arr):
    pred = model.predict(arr)
    return pred


#per = predict_pipeline(np.array([30, 87000]).reshape(1, -1))
#per = predict_pipeline(X_test[:20])
#print(per[0])
