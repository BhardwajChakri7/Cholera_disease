import pickle
import streamlit as st

# Load the saved model
Cholera_project = pickle.load(open('Cholera_model.sav', 'rb'))

# Page title
st.markdown("<h1 style='text-align: center; color: white;'>Cholera Disease Prediction using ML</h1>", unsafe_allow_html=True)

# Input data from the user
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Gender = st.text_input('Gender')

    with col3:
        Access_to_Clean_Water = st.text_input('Access to Clean Water')

    with col4:
        Sanitation_Facilities = st.text_input('Sanitation Facilities')

    with col5:
        Proximity_to_Water_Source = st.text_input('Proximity to Water Source')

    with col1:
        Population_Density = st.text_input('Population Density')

    with col2:
        Income_Level = st.text_input('Income Level')

    with col3:
        Education_Level = st.text_input('Education Level')

    with col4:
        Housing_Conditions = st.text_input('Housing Conditions')

    with col5:
        Season = st.text_input('Season')

    with col1:
        Pre_existing_Conditions = st.text_input('Pre-existing Conditions')

    with col2:
        Vaccination_Status = st.text_input('Vaccination Status')

    with col3:
        Access_to_Healthcare = st.text_input('Access to Healthcare')

# Code for prediction
Cholera_diagnosis = ''

# Prediction button
if st.button('Cholera Disease Test Button'):
    try:
        Cholera_disease_prediction = Cholera_project.predict([[  
            Age, Gender, Access_to_Clean_Water, Sanitation_Facilities,
            Proximity_to_Water_Source, Population_Density, Income_Level,
            Education_Level, Housing_Conditions, Season,
            Pre_existing_Conditions, Vaccination_Status, Access_to_Healthcare
        ]])
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
        max-width: 800px;
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
        box-sizing: border-box;
    }
    select {
        height: 45px;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
