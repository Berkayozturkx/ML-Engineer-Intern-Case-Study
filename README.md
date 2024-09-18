# Amazon Hisse Senedi Tahmin Uygulaması

Bu proje, FastAPI ve Streamlit kullanarak Amazon hisse senedi tahminleri yapmayı amaçlayan bir uygulamadır. LSTM modelini kullanarak 7 günlük hisse senedi verilerine dayalı tahminler yapabilirsiniz. Uygulama, FastAPI üzerinde çalışan bir API ve bu API'yi çağıran bir Streamlit ön yüzünden oluşmaktadır.

## Özellikler

- **FastAPI API**: Amazon hisse senedi tahminlerini gerçekleştiren LSTM modeline dayalı bir API.
- **Streamlit Ön Yüzü**: Kullanıcıların API'yi kolayca kullanabilmesi için basit ve sezgisel bir web arayüzü.
- **Hata Yönetimi**: Girilen verilerin doğruluğunu kontrol eden ve uygun olmayan durumlarda kullanıcıya anlamlı hata mesajları dönen bir sistem.
- **Tahmin Hassasiyeti**: Tahmin edilen değeri iki ondalık basamakla döner.

## Gereksinimler

Bu uygulamanın çalışabilmesi için aşağıdaki yazılımların yüklü olması gerekmektedir:

1. **Amazon Stock Price Forecasting.ipynb Dosyasının Çalışabilmesi için Gerekli Kütüphaneler**
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow
- Statsmodels
- Keras

2. **Uygulama için Gerekli Kütüphaneler**
- Python 3.x
- TensorFlow
- Streamlit
- FastAPI
- Uvicorn
- Pydantic

## Kurulum

Bu uygulamayı çalıştırmak için aşağıdaki adımları izleyin:

1. **Python ve Paketlerin Yüklenmesi:**
   Eğer Anaconda kullanıyorsanız, aşağıdaki komutu kullanarak bir sanal ortam oluşturabilir ve gerekli paketleri yükleyebilirsiniz:

   ```
   conda create -n sanal_ortam_ismi
   conda activate sanal_ortam_ismi
2. **Daha sonra, gerekli paketleri yüklemek için:**
    Dosyanın bulunduğu dizine gidip aşağıdaki komutları kullanarak gereksinimleri yükleyebilirsiniz:
    ```
    pip install -r requirements.txt
3. **Model Dosyasının Yüklenmesi:**
`LSTM_Best_model.keras` adlı LSTM model dosyanızın uygulamanızın bulunduğu dizinde yer aldığından emin olun. Bu model, tahminler yapmak için kullanılacaktır.
4. **FastAPI'yi Çalıştırma:**
    Komut satırında dosyanın bulunduğu dizine gidip FastAPI uygulamasını başlatmak için aşağıdaki komutu çalıştırın:
    ```
    uvicorn app:app --reload
5. **Streamlit'i Çalıştırma:**
    Komut satırında dosyanın bulunduğu dizine gidip Streamlit ön yüz uygulamasını başlatmak için aşağıdaki komutu çalıştırın:
    ```
    streamlit run app_frontend.py
## Kullanım
1. **API Üzerinden Kullanım:**
    `http://127.0.0.1:8000/docs#/` adresine gidin ve "/predict/" sekmesine tıklayın. Ardından açılan pencereden "Try it out" butonuna basın. Daha sonra aktif olan request body'deki values kısmına değerleri girin ve "Execute" butonuna basın.
    ![api_kullanim](https://github.com/user-attachments/assets/6b25b13a-4f35-43e5-860c-cf5e152c60a3)
2. **Streamlit Ön Yüzü Üzerinden Kullanım:**
    `uvicorn app:app --reload` komutu ile FastAPI'yı ve `streamlit run app_frontend.py` komutu ile Streamlit API Ön Yüzü'nü çalıştırdıktan sonra `http://localhost:8501` adresine gidin. Ardından ilgili kutucuklara hisse fiyatlarını girin ve "Tahmin Et" butonuna basın.
![streamlit_kullanim](https://github.com/user-attachments/assets/c6e941dc-c1bc-4168-a215-d772bb1e5faf)