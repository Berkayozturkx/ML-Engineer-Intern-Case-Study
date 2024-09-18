import streamlit as st
import requests

# FastAPI'nin URL'si
API_URL = "http://127.0.0.1:8000/predict/"

st.title("LSTM Amazon Hisse Senedi Tahmin Arayüzü")

# Kullanıcıdan veri girişi
values = []
for i in range(7):
    value = st.number_input(f"{7-i} Gün Önceki Hisse Senedi Fiyatı:", format="%f", step=0.01)
    values.append(value)

# Buton
if st.button("Tahmin Et"):
    try:
        # API'ye veri gönderme
        response = requests.post(API_URL, json={"values": values})
        response.raise_for_status()  # Hata varsa exception fırlatır
        data = response.json()
        
        # Tahmin edilen değeri gösterme
        st.write(f"Tahmin Edilen Değer: {data['predicted_value']:.2f}")
        
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP hata oluştu: {http_err}")
    except Exception as err:
        st.error(f"Bir hata oluştu: {err}")