import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide')

# Load Models
diabetes_model = pickle.load(open(r"D:\Shrihi\Internships\AICTE - Prediction\Prediction of disease\sav - save models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"D:\Shrihi\Internships\AICTE - Prediction\Prediction of disease\sav - save models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"D:\Shrihi\Internships\AICTE - Prediction\Prediction of disease\sav - save models\parkinsons_model.sav", 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(' Prediction of Disease Outbreak System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital.fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# Parkinson's Prediction Section
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction Using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:FO(HZ)', key='fo')
        RAP = st.text_input('MDVP:RAP', key='rap')
        shimmer_APQ3 = st.text_input('Shimmer:APQ3', key='shimmer_apq3')
        HNR = st.text_input('HNR', key='hnr')
        D2 = st.text_input('D2', key='d2')
    
    with col2:
        fhi = st.text_input('MDVP:FHI(HZ)', key='fhi')
        PPQ = st.text_input('MDVP:PPQ', key='ppq')
        shimmer_APQ5 = st.text_input('Shimmer:APQ5', key='shimmer_apq5')
        RPDE = st.text_input('RPDE', key='rpde')
        PPE = st.text_input('PPE', key='ppe')

    with col3:
        flo = st.text_input('MDVP:FLO(HZ)', key='flo')
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', key='jitter_abs')
        shimmer_APQ = st.text_input('Shimmer:APQ', key='shimmer_apq')
        DFA = st.text_input('DFA', key='dfa')
    
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', key='jitter_percent')
        Jitter_PPQ = st.text_input('MDVP:PPQ (Jitter)', key='jitter_ppq')  # Added unique key
        shimmer = st.text_input('MDVP:Shimmer', key='shimmer')
        spread1 = st.text_input('Spread1', key='spread1')
    
    with col5:
        shimmer_dB = st.text_input('MDVP:Shimmer(dB)', key='shimmer_db')
        shimmer_DDA = st.text_input('Shimmer:DDA', key='shimmer_dda')
        NHR = st.text_input('NHR', key='nhr')
        spread2 = st.text_input('Spread2', key='spread2')

    if st.button('Parkinsons Test Result'):
        required_fields = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, Jitter_PPQ, shimmer, shimmer_dB, 
                           shimmer_APQ3, shimmer_APQ5, shimmer_APQ, shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        if '' in required_fields:
            st.error("Please ensure all input fields are filled.")
        else:
            try:
                user_input = list(map(float, required_fields))
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    st.success('The person has Parkinson’s disease.')
                else:
                    st.success('The person does not have Parkinson’s disease.')
            except ValueError:
                st.error("Please ensure all input fields contain numeric values.")
