import streamlit as st
import pickle
import pandas as pd


st.title('First Streamlit App for Machine Learning')

st.write('This web app predicts the **House Price** in the California Region for XYZ Brokerage')

#to read the model from the pickle file
model=pickle.load(open('model_lr.pkl','rb'))

# get input from the user

med_inc=st.number_input('Median Income')
house_age=st.number_input('House Age')
ave_room=st.number_input('Ave Rooms')
ave_bedrms=st.number_input('Ave Bedrooms')
population=st.number_input('Population')
ave_occup=st.number_input('Ave Occupation')
latitude=st.number_input('Latitude')
longitude=st.number_input('Longitude')

# convert the user information in DataFrame
user_data=pd.DataFrame({'MedInc':med_inc,
    'HouseAge':house_age,
    'AveRooms':ave_room,
    'AveBedrms':ave_bedrms,
    'Population':population,
    'AveOccup':ave_occup,
    'Latitude':latitude,
    'Longitude':longitude}, index=[0])

# predict the house proce
prediction=model.predict(user_data)

if st.button('Predict'):
    st.write(f'The predict house price is {prediction[0]*100000}')