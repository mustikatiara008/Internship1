import pickle
import streamlit as st

# membaca model
vendor_model = pickle.load(open('vendor_model.sav', 'rb'))


#judul aplikasi
st.title('Prediksi Keterlambatan Vendor')

Conditions  = st.text_input ('Input nilai kondisi')

Weather_Condition  = st.text_input ('Input nilai cuaca')

Delivery_Distance_Km  = st.text_input ('Input nilai jarak pengiriman')


# code for prediction

vend_diagnosisi = ''

# button for prediction
if st.button('Test Prediksi Keterlambatan Vendor'):
    vend_prediction = vendor_model.predict([[ Conditions, Weather_Condition, Delivery_Distance_Km]])

    if(vend_prediction[0] == 1):
        vend_diagnosisi = 'Vendor Terlambat'
    else :
        vend_diagnosisi = 'Vendor Tidak Terlambat'
        
    st.success(vend_diagnosisi)
    

