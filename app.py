import streamlit as st

st.title('Calculate Your BMI') 
wt = st.number_input('Enter your wieght in kgs:')
h = st.number_input('Enter your height in CMS:')
if h==0:
    bmi =0
else:
    bmi = wt/h**2 
st.success(f'Your BMI is {bmi} Kg/m^2')