import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Cholera_project = pickle.load(open('Cholera_model.sav', 'rb'))
# page title
st.title('Cholera Disease Prediction using ML')


# getting the input data from the user
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    Age = st.text_input('Age')
    
with col2:
    Gender = st.text_input('Gender')

with col3:
    Access_to_Clean_Water = st.text_input('Access_to_Clean Water')
    
with col4:
    Sanitation_Facilities = st.text_input('Sanitation_Facilities')
    
with col5:
    Proximity_to_Water_Source = st.text_input('Proximity_to_Water_Source')

with col1:
    Population_Density = st.text_input('Population_Density')
    
with col2:
    Income_Level = st.text_input('Income_Level')

with col3:
    Education_Level = st.text_input('Education_Level')

with col4:
    Housing_Conditions = st.text_input('Housing_Conditions')

with col5:
    Season = st.text_input('Season')
    
with col1:
    Pre_existing_Conditions = st.text_input('Pre_existing_Conditions')

with col2:
    Vaccination_Status = st.text_input('Vaccination_Status')
    
with col3:
    Access_to_Healthcare = st.text_input('Access_to_Healthcare')
    
# code for Prediction
Cholera_diagnosis = ''

# creating a button for Prediction

if st.button('Cholera Disease Test Button'):
    try:
        Cholera_disease_prediction = Cholera_project.predict([[Age,Gender,Access_to_Clean_Water,Sanitation_Facilities,Proximity_to_Water_Source,Population_Density,Income_Level,Education_Level,Housing_Conditions,Season,Pre_existing_Conditions,Vaccination_Status,Access_to_Healthcare]])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if (Cholera_disease_prediction[0] == 1):
      Cholera_diagnosis = 'The person is effected with Cholera'
    else:
      Cholera_diagnosis = 'The person is not effected with Cholera'
    
st.success(Cholera_diagnosis)
