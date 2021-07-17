# setup 

import re
import numpy as np
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline, make_pipeline
import matplotlib.pyplot as plt
from streamlit.elements import selectbox


# Load Dataset
df = pd.read_csv("train.csv")

## Data preprocessing
X = df[['Household Number', 'Age', 'Region_N', 'Area_type_N', 'Gender_N',
       'Marital_N', 'Credit_N', 'Saving_N',
       'Remittances_N', 'Education_N', 'Income_Sources_N', 'Q1213_N']]
y = df['Banked/Unbanked_N']

## Model pipeline
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X_train,y_train)

train_score = pipe.score(X_train, y_train)
test_score = pipe.score(X_test, y_test)
y_predict = pipe.predict(X_test)

## Title
st.title("Omdena Banking The unbanked")
st.subheader("Scores For Pretrained Models")
st.subheader("1. Logistic Regression")

st.subheader("Train set Score: {}".format( round(train_score, 3)))
st.subheader("Test set Score: {}".format( round(test_score, 3)))

## Take input from users
st.sidebar.header("Take input from users")
Name = st.sidebar.text_input("Name of User")
Region = st.sidebar.selectbox('Region', options=['Greater Accra', 'Ashanti', 'Western', 'Central', 'Volta','Eastern', 'Upper West', 'Brong Ahafo', 'Northern', 'Upper East'])
Area_type = st.sidebar.selectbox('Area Type', options=['Urban', 'Rural'])
House_Hold_Number = st.sidebar.slider('Household Number', 1, 15)
age = st.sidebar.slider("Age", 1, 100)
gender = st.sidebar.selectbox('Gender', options=['Male', 'Female'])
education = st.sidebar.selectbox('Education Level', options=['Primary education', 'Secondary education', 'No formal education',
       'Other/Dont know', 'Vocational/Specialised training',
       'Tertiary education'])
marital = st.sidebar.selectbox("Marital Status", options=['Married', 'Divorced', 'Never married', 'Widowed','Not Answered/Missing data', 'Separated'])
credit = st.sidebar.selectbox('Where do you take credit', options=['Credit from family and friends', 'Not borrowing','Credit from other formal (non-bank)','Credit from informal sources', 'Credit from bank'])
saving = st.sidebar.selectbox('Where Do you keep your savings', options=['Saving at bank', 'Saving informally', 'Not saving','Saving at other formal (non-bank)', 'Saving at home'])
remittance = st.sidebar.selectbox('Form of Remittance', options=['Not remitting', 'Remitting informally','Remiting through family and friends', 'Remitting through bank','Remitting through other formal (non-bank)'])
income_sources = st.sidebar.selectbox('Income Source', options=['Formally employed Private', 'Farming and Fishing',
       'Self employed', 'Remittance Dependent', 'Informally employed',
       'Other Income', 'Dont Know'])
income_level = st.sidebar.selectbox('Income Level', options=['Below GH¢200 per month', 'GH¢201 - GH¢400 per month', 'No income',
       'GH¢401 - GH¢600 per month', 'Over GH¢2201 per month',
       'GH¢601 - GH¢800 per month', 'GH¢801 - GH¢1000 per month',
       'GH¢1001 - GH¢1200 per month', 'GH¢1801 - GH¢2000 per month',
       'GH¢2001 - GH¢2200 per month', 'GH¢1201 - GH¢1400 per month',
       'GH¢1401 - GH¢1600 per month', 'GH¢1601 - GH¢1800 per month'])       

## convert categorical features to numerical features
# Region
if Region == 'Greater Accra':
    Region = 4
elif Region == 'Ashanti':
    Region = 0
elif Region == 'Western':
    Region = 9
elif Region == 'Central':
    Region = 2
elif Region == 'Volta':
    Region = 8
elif Region == 'Eastern':
    Region = 3
elif Region == 'Upper West':
    Region = 7
elif Region == 'Brong Ahafo':
    Region = 1 
elif Region == 'Northern':
    Region = 5
else:
    Region = 6    
# Area_type
if Area_type == 'Urban':
    Area_type = 1
else: 
    Area_type = 0 

# sex
if gender == 'Male':
    gender = 1
else: 
    gender = 0       

# education
if education == 'Primary education':
    education = 2
elif education == 'Secondary education':
    education = 3
elif education == 'No formal education':
    education = 0
elif education == 'Other/Dont know':
    education = 1 
elif education == 'Vocational/Specialised training':
    education = 5
else:
    education = 4    
# marital
if marital == 'Married':
    marital = 1
elif marital == 'Divorced':
    marital = 0
elif marital == 'Never married':
    marital = 2 
elif marital == 'Widowed':
    marital = 4 
else:
    marital = 3  
# saving
if saving == 'Saving at bank':
    saving = 1
elif saving == 'Saving informally':
    saving = 4
elif saving == 'Not saving':
    saving = 0
elif saving == 'Saving at other formal (non-bank)':
    saving = 3
else:
    saving = 2     
# credit
if credit == 'Credit from family and friends':
    credit = 1
elif credit == 'Not borrowing':
    credit = 4
elif credit == 'Credit from other formal (non-bank)':
    credit = 3 
elif credit == 'Credit from informal sources':
    credit = 2 
else:
    credit = 0   
# remittance
if remittance == 'Not remitting':
    remittance = 0
elif remittance == 'Remitting informally':
    remittance = 2
elif remittance == 'Remiting through family and friends':
    remittance = 1 
elif remittance == 'Remitting through other formal (non-bank)':
    remittance = 4 
else:
    remittance = 3  
# income_sources
if income_sources == 'Formally employed Private':
    income_sources = 2
elif income_sources == 'Farming and Fishing':
    income_sources = 1
elif income_sources == 'Self employed':
    income_sources = 6
elif income_sources == 'Remittance Dependent':
    income_sources = 5
elif income_sources == 'Informally employed':
    income_sources = 3 
elif income_sources == 'Other Income':
    income_sources = 4    
else:
    income_sources = 0  
# income_level
if income_level == 'Below GH¢200 per month':
    income_level = 0
elif income_level == 'GH¢201 - GH¢400 per month':
    income_level = 7
elif income_level == 'No income':
    income_level = 11
elif income_level == 'GH¢401 - GH¢600 per month':
    income_level = 8
elif income_level == 'Over GH¢2201 per month':
    income_level = 12 
elif income_level == 'GH¢601 - GH¢800 per month':
    income_level = 9   
elif income_level == 'GH¢801 - GH¢1000 per month':
    income_level = 10
elif income_level == 'GH¢1001 - GH¢1200 per month':
    income_level = 1
elif income_level == 'GH¢1801 - GH¢2000 per month':
    income_level = 5
elif income_level == 'GH¢2001 - GH¢2200 per month':
    income_level = 6 
elif income_level == 'GH¢1201 - GH¢1400 per month':
    income_level = 2
elif income_level == 'GH¢1401 - GH¢1600 per month':
    income_level = 3    
else:
    income_level = 4  

# final model
input_data = [[House_Hold_Number,age,Region, Area_type, gender,
       marital, credit, saving,
       remittance, education,income_sources, income_level]]
prediction = pipe.predict(input_data)
predict_probability = pipe.predict_proba(input_data)

if prediction[0] == 1:
       st.subheader("Hello, {} we have predicted you are Banked with a probability of {}%".format(Name, round(predict_probability[0][1] * 100, 3)))
else:
       st.subheader("Hello, {} we have predicted you are UnBanked with a probability of {}%".format(Name, round(predict_probability[0][0] * 100, 3)))

st.header(input_data)
# Model 2
st.subheader("1. Random Forest Model")
from sklearn.metrics import confusion_matrix, accuracy_score

# fit and Evaluate model
from xgboost import XGBClassifier
my_model2 = XGBClassifier(min_child_weight = 1, gamma = 2, subsample = 1.0,
                          colsample_bytree = 0.8, max_depth = 3, use_label_encoder=False)
my_model2.fit(X_train, y_train)
y_pred2 = my_model2.predict(X_test)

train_score2 = my_model2.score(X_train, y_train)
test_score2 = my_model2.score(X_test, y_test)


st.subheader("Train set Score: {}".format( round(train_score2, 3)))
st.subheader("Test set Score: {}".format( round(test_score2, 3)))

# final model
prediction2 = my_model2.predict(np.array(input_data))
predict_probability = my_model2.predict_proba(np.array(input_data))

if prediction[0] == 1:
       st.subheader("Hello, {} we have predicted you are Banked with a probability of {}%".format(Name, round(predict_probability[0][1] * 100, 3)))
else:
       st.subheader("Hello, {} we have predicted you are UnBanked with a probability of {}%".format(Name, round(predict_probability[0][0] * 100, 3)))


