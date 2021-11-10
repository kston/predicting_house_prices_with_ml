import streamlit as st
from datetime import date

st.title('Predicting House Price with ML')

MSSubClass_options ={ "2-STORY 1946 & NEWER" :20 , "SPLIT OR MULTI-LEVEL" : 60}

MSSubClass=st.sidebar.selectbox("Identifies the type of dwelling involved in the sale.",MSSubClass_options)


MSZoning_options = { "Residential High Density" :'RH' , "Commercial" : 'C'}

MSZoning=st.sidebar.selectbox("Identifies the general zoning classification of the sale.", MSZoning_options)



LotFrontage = st.sidebar.slider('Linear feet of street connected to property', 0, 100, 10)


LotShape_options = ['Reg', 'IR1']
LotShape=st.sidebar.selectbox("General shape of property", LotShape_options)


LandContour_options = ['Lvl', 'Low']
LandContour=st.sidebar.selectbox("Flatness of the property", LandContour_options)



LotConfig_options = ['Inside', 'Inside']
LotConfig=st.sidebar.selectbox("Lot configuration", LotConfig_options)


Neighborhood_options = { "Briardale" :'BrDale' , "Brookside" : 'BrkSide'}
Neighborhood=st.sidebar.selectbox("Lot configuration", Neighborhood_options)



OverallQual = st.sidebar.slider('Rates the overall material and finish of the house', 0, 10, 1)

OverallCond = st.sidebar.slider('Rates the overall condition of the house', 0, 10, 1)

#YearBuilt = st.sidebar.slider('Rates the overall condition of the house', date(1921,1,1), date(2021,12,31), 1)






"""

       
    

    
    
    'KitchenQual',
    
    KitchenQual: Kitchen quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       
       
    TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
    
    
    'FireplaceQu',
    
    FireplaceQu: Fireplace quality

       Ex	Excellent - Exceptional Masonry Fireplace
       Gd	Good - Masonry Fireplace in main level
       TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
       Fa	Fair - Prefabricated Fireplace in basement
       Po	Poor - Ben Franklin Stove
       NA	No Fireplace
       
       
    'GarageFinish',
    
    GarageFinish: Interior finish of the garage

       Fin	Finished
       RFn	Rough Finished	
       Unf	Unfinished
       NA	No Garage
       
       
    'PavedDrive',
    
    PavedDrive: Paved driveway

       Y	Paved 
       P	Partial Pavement
       N	Dirt/Gravel
       
       
    'WoodDeckSF',
    
    WoodDeckSF: Wood deck area in square feet


    'ScreenPorch',
    
    
ScreenPorch: Screen porch area in square feet


    'SaleCondition',
    
    SaleCondition: Condition of sale

       Normal	Normal Sale
       Abnorml	Abnormal Sale -  trade, foreclosure, short sale
       AdjLand	Adjoining Land Purchase
       Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit	
       Family	Sale between family members
       Partial	Home was not completed when last assessed (associated with New Homes)

    
    YrSold: Year Sold (YYYY)
    

"""
   