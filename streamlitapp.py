import pickle
import streamlit as st
import pandas as pd

# Load the saved model
Cholera_project = pickle.load(open('Cholera_model.sav', 'rb'))

# Page title
st.markdown("<h1 style='text-align: center; color: white;'>Cholera Disease Prediction</h1>", unsafe_allow_html=True)

# Input data from the user
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Age = st.number_input('Age', min_value=0, max_value=120, value=30)

    with col2:
        Gender = st.selectbox('Gender', options=['Male', 'Female', 'Other'], index=0)

    with col3:
        Access_Clean_Water = st.selectbox('Access to Clean Water', options=['Yes', 'No'], index=0)

    with col4:
        Sanitation = st.selectbox('Sanitation Facilities', options=['Good', 'Average', 'Poor'], index=1)

    with col5:
        Proximity_Water = st.number_input('Distance to Water (km)', min_value=0.0, max_value=100.0, value=1.0)

    with col1:
        Access_Healthcare = st.selectbox('Access to Healthcare', options=['Yes', 'No'], index=0)

    with col2:
        Income_Level = st.selectbox('Income Level', options=['Low', 'Medium', 'High'], index=1)

    with col3:
        Education = st.selectbox('Education Level', options=['No Education', 'Primary', 'Secondary', 'Tertiary'], index=2)

    with col4:
        Housing_Conditions = st.selectbox('Housing Conditions', options=['Good', 'Average', 'Poor'], index=1)

    with col5:
        Season = st.selectbox('Season', options=['Winter', 'Spring', 'Summer', 'Fall'], index=2)

    with col1:
        Pre_Conditions = st.selectbox('Pre-existing Conditions', options=['None', 'Chronic', 'Other'], index=0)

    with col2:
        Vaccination_Status = st.selectbox('Vaccination Status', options=['Vaccinated', 'Not Vaccinated'], index=0)

    with col3:
        Pop_Density = st.number_input('Population Density (people/km²)', min_value=0, max_value=10000, value=100)

# Code for prediction
Cholera_diagnosis = ''

# Prediction button
if st.button('Test for Cholera'):
    try:
        # Prepare the input for prediction
        input_data = pd.DataFrame({
            'Age': [Age],
            'Gender': [Gender],
            'Access_Clean_Water': [Access_Clean_Water],
            'Sanitation': [Sanitation],
            'Proximity_Water': [Proximity_Water],
            'Pop_Density': [Pop_Density],
            'Income_Level': [Income_Level],
            'Education': [Education],
            'Housing_Conditions': [Housing_Conditions],
            'Season': [Season],
            'Pre_Conditions': [Pre_Conditions],
            'Vaccination_Status': [Vaccination_Status],
            'Access_Healthcare': [Access_Healthcare]
        })

        # Convert categorical variables to numerical (if needed)
        input_data['Gender'] = input_data['Gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
        input_data['Access_Clean_Water'] = input_data['Access_Clean_Water'].map({'Yes': 1, 'No': 0})
        input_data['Sanitation'] = input_data['Sanitation'].map({'Good': 2, 'Average': 1, 'Poor': 0})
        input_data['Income_Level'] = input_data['Income_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})
        input_data['Education'] = input_data['Education'].map({'No Education': 0, 'Primary': 1, 'Secondary': 2, 'Tertiary': 3})
        input_data['Housing_Conditions'] = input_data['Housing_Conditions'].map({'Good': 2, 'Average': 1, 'Poor': 0})
        input_data['Season'] = input_data['Season'].map({'Winter': 0, 'Spring': 1, 'Summer': 2, 'Fall': 3})
        input_data['Pre_Conditions'] = input_data['Pre_Conditions'].map({'None': 0, 'Chronic': 1, 'Other': 2})
        input_data['Vaccination_Status'] = input_data['Vaccination_Status'].map({'Vaccinated': 1, 'Not Vaccinated': 0})
        input_data['Access_Healthcare'] = input_data['Access_Healthcare'].map({'Yes': 1, 'No': 0})

        Cholera_disease_prediction = Cholera_project.predict(input_data)
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    else:
        if Cholera_disease_prediction[0] == 1:
            Cholera_diagnosis = 'The person is affected with Cholera'
        else:
            Cholera_diagnosis = 'The person is not affected with Cholera'

st.success(Cholera_diagnosis)

# Apply styles
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    .block-container {
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border: 2px solid #ccc;
        border-radius: 15px;
        max-width: 900px;
        margin: auto;
        backdrop-filter: blur(10px);
        box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7);
    }
    .stButton>button {
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        padding: 12px 30px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF6347;
        border: 2px solid #FF6347;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    input[type="text"], input[type="number"], select {
        background-color: white !important;
        color: black !important;
        border: 1px solid #FF6347;
        border-radius: 5px;
        padding: 12px;
        width: 100%;
        max-width: 250px; /* Increase max width for input boxes */
        box-sizing: border-box;
    }
    select {
        height: 45px;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
    }
    label {
        margin-bottom: 10px; /* Increase space below input titles */
    }
    </style>
    """,
    unsafe_allow_html=True
)
