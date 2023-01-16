from fastapi import FastAPI
from pydantic import BaseModel
#from app.model import predict_pipeline
#from app.model import __version__ as model_version #when run in docker
from model import predict_pipeline
from model import __version__ as model_version #when run within code
#from typing import List


app = FastAPI()


class FeatureIn(BaseModel):
    age: float
    salary: float


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict") #'http://127.0.0.1:8080/predict'
def predict(input_data: FeatureIn):
    test_data = [[
        input_data.age,
        input_data.salary
    ]]
    class_idx = predict_pipeline(test_data)[0]
    class_idx = int(class_idx)
    return {"class_index": class_idx}

#open app directory first run fastapi app then run stream_app
# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
