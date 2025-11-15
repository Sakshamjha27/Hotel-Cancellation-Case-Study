import numpy as np 
import pandas as pd
import streamlit as st 
import joblib 

#lets load all the instances req over here 

with open('transformer.joblib','rb') as file :
    transformer = joblib.load(file) 
    
#lets load the model 

with open('final_model.joblib','rb') as file :
    model = joblib.load(file) 
    
st.title('Inn Hotel Group')
st.header('Thi application wll predicted the chances of booking cancellelations')

#lets take input from the user 
amnth = st.slider('Select your month r arrival',min_vlaue = 1 , max_value= 12)
wkd_lambda = (lambda x:0 if x=='Mon' else 
              1 if x=='Tue' else 
              2 if x=='Weds' else 
              3 if x=='Thrus' else 
              4 if x=='Fri' else 
              5 if x=='Sat' else 
              6) 
awkd = st.selectbox('select your weekday of arrival',['Mon','Tues','Weds','Thrus','Fri','Sat','Sun']) 
dwkd = st.selectbox('select your weekday of departure',['Mon','Tues','Weds','Thrus','Fri','Sat','Sun']) 
wkend = st.number_input('Enter How many weekend nights are there in stay',min_values=0)
wk = st.number_input('Enter How many weekend nights are there in stay',min_values=0)
totn = wkend + wk 
mkt = (lambda x: 0 if x=='Ofline' else 1 )(st.selectbox('How is booking took place?',['Offline','Online']))
lt = st.number_input('how many days prior booking was done?',min_value = 0 )
price = st.number_input('What i tha avg price?',min_value=0) 
adults = st.number_input('how many adult members in booking',min_value = 1)
spcl = st.selectbox('How maNy select request maade ?',[0,1,2,3,4,5])
park = (lambda x:0 if x=='No' else 1)(st.selectbox('How guest need parking spaces',['Yes','No']))

#Transform the data
lt_t,price_t = transformer.tranform([[lt,price]])[0]


# Create the input list 
input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth,awkd,totn,dwkd]

#Make predictions
predictions = model.predict_proba([input_list])[:,1][0]

#lets show the probabality 
if st.button('Predict'):
    st.success(f'Cancellation Chances: {round(predictions,4)*100}%')
    