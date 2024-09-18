from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf

# FastAPI uygulaması oluşturma
app = FastAPI()

# Pydantic modeli - Girdi verileri için
class PredictionInput(BaseModel):
    # Girilen değerler float olmadığında otomatik olarak hata verecek.
    values: list[float]

# LSTM modelini yükleme
model = tf.keras.models.load_model('LSTM_Best_Model.keras')

@app.get("/")
def read_root():
    return {"message": "LSTM Amazon Hisse Senedi Tahmin API'sine Hoş Geldiniz."}

@app.post("/predict/")
async def predict(input_data: PredictionInput):
    # Verileri alma
    data = input_data.values

    # 7 değer girilip girilmediğini kontrol etme
    if len(data) != 7:
        raise HTTPException(status_code=400, detail="Tam olarak 7 değer girilmelidir.")

    # Girilen değerlerin pozitif olup olmadığını kontrol etme
    if any(x <= 0 for x in data):
        raise HTTPException(status_code=400, detail="Değerlerin tümü pozitif olmalıdır.")
    

    # Veriyi reshape etme
    reshaped_data = np.array(data).reshape(1, 1, 7)

    # Tahmin yapma işlemi
    prediction = model.predict(reshaped_data)

    # Tahmin edilen değeri 2 ondalık basamağa yuvarlama ve float'a dönüştürme
    prediction_value = round(float(prediction[0, 0]), 2)

    return {"predicted_value": prediction_value}