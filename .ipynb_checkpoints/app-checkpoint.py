import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

import joblib


st.title('Predicting House Price with ML')

# Sidebar components
## Sidebar Title
st.sidebar.markdown("<h1 style='text-align: center; color: black; display:block;'>House Data</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

## Categorical Features


st.sidebar.markdown("<p style='text-align: left; color: black; font-weight: bold; display:block;'>Categorical Features </p>", unsafe_allow_html=True)

MSSubClass_options ={ "2-STORY 1946 & NEWER" :20 , "SPLIT OR MULTI-LEVEL" : 60}

MSSubClass=st.sidebar.selectbox("Identifies the type of dwelling involved in the sale.",MSSubClass_options)

MSZoning_options = { "Residential High Density" :'RH' , "Commercial" : 'C'}
MSZoning=st.sidebar.selectbox("Identifies the general zoning classification of the sale.", MSZoning_options)

LotShape_options = ['Reg', 'IR1']
LotShape=st.sidebar.selectbox("General shape of property", LotShape_options)

LandContour_options = ['Lvl', 'Low']
LandContour=st.sidebar.selectbox("Flatness of the property", LandContour_options)

LotConfig_options = ['Inside', 'Inside']
LotConfig=st.sidebar.selectbox("Lot configuration", LotConfig_options)

Neighborhood_options = { "Briardale" :'BrDale' , "Brookside" : 'BrkSide'}
Neighborhood=st.sidebar.selectbox("Lot configuration", Neighborhood_options)


GarageFinish_options = {'Finished': 'Fin', 'Rough Finished': 'RFn', 'Unfinished':'Unf', 'No Garage': 'NA'  }
GarageFinish = st.sidebar.selectbox("Interior finish of the garage", GarageFinish_options)


PavedDrive_options = {'Paved': 'Y', 'Partial Pavement': 'P', 'Dirt/Gravel':'N'}
PavedDrive = st.sidebar.selectbox("Paved driveway", PavedDrive_options)


SaleCondition_options =  {'Normal Sale': 'Normal', 'Sale between family members': 'Family'}
SaleCondition = st.sidebar.selectbox("Condition of sale", SaleCondition_options)



KitchenQual_options =  ['Ex', 'Gd', 'TA', 'Fa', 'Po']

KitchenQual = st.sidebar.selectbox("Kitchen quality", KitchenQual_options)


FireplaceQu_options =  ['Ex', 'Gd', 'TA', 'Fa', 'Po']

FireplaceQu = st.sidebar.selectbox("Fireplace quality", FireplaceQu_options)


st.sidebar.markdown("<hr>", unsafe_allow_html=True)

## Numerical Features


st.sidebar.markdown("<p style='text-align: left; color: black; font-weight: bold;'>Numerical Features </p>", unsafe_allow_html=True)


LotFrontage = st.sidebar.slider('Linear feet of street connected to property', 0, 100, 10)

OverallQual = st.sidebar.slider('Rates the overall material and finish of the house', 0, 10, 1)

OverallCond = st.sidebar.slider('Rates the overall condition of the house', 0, 10, 1)

YearBuilt = st.sidebar.slider('Original construction date', min_value = 1921, max_value = 2021, step= 1 )

TotRmsAbvGrd = st.sidebar.slider('Total rooms above grade (does not include bathrooms)', 0, 20, 1)


WoodDeckSF = st.sidebar.slider('Wood deck area in square feet', 0, 100,1)

ScreenPorch = st.sidebar.slider('Screen porch area in square feet', 0, 100,1)

YrSold = st.sidebar.slider('Year Sold (YYYY)', min_value = 1960, max_value = 2021, step= 1)


st.sidebar.markdown("<hr>", unsafe_allow_html=True)


st.sidebar.markdown("""
<style>
div.stButton > button:first-child {
      text-align: center;
      font-size: 14px;
      margin: 4px 20px;
      position: relative;
      padding: 10px 100px;
      font-weight: bold;
      
}
</style>""", unsafe_allow_html=True)

submit = st.sidebar.button("Predict")

if submit:
    st.success("Prediction Done")
    features = [
        MSSubClass,
        MSZoning,
        LotShape,
        LandContour,
        LotConfig,
        Neighborhood,
        GarageFinish,
        PavedDrive,
        SaleCondition,
        FireplaceQu,
        LotFrontage,
        OverallQual,
        OverallCond,
        YearBuilt,
        TotRmsAbvGrd,
        WoodDeckSF,
        ScreenPorch,
        YrSold    
    ]
    
    head = [
        'MSSubClass',
        'MSZoning',
        'LotShape',
        'LandContour',
        'LotConfig',
        'Neighborhood',
        'GarageFinish',
        'PavedDrive',
        'SaleCondition',
        'FireplaceQu',
        'LotFrontage',
        'OverallQual',
        'OverallCond',
        'YearBuilt',
        'TotRmsAbvGrd',
        'WoodDeckSF',
        'ScreenPorch',
        'YrSold'    
    ]
    
    df=pd.DataFrame(features).transpose()
    df.columns = head
    st.markdown("<h3 style='text-align: center; color: black; display:block;'> Informed Datas</h3>", unsafe_allow_html=True)
    st.dataframe(df)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black; display:block;'> Predicted Price</h3>", unsafe_allow_html=True)
    
    # tranform categorical data
    def transform_categorical(list):
        for feature in list:
            dict_key = globals()[f'{feature}_options']
            df[feature] = dict_key[df[feature].values[0]]
           
    transform_categorical(['MSSubClass', 'MSZoning', 'GarageFinish', 'PavedDrive', 'SaleCondition'])       
        
    model = joblib.load('price_pipe.pkl')
    prediction = list(model.predict(df))
    print(prediction)
   
        

             
           
             
            
    
        
     
    
    
  
   
    
    
