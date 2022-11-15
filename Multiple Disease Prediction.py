import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import sklearn
from sklearn.preprocessing import MinMaxScaler,StandardScaler


# loading the saved models

diabetes_model = pickle.load(open(r"C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\diabetes_model.pkl", 'rb'))

heart_disease_model = pickle.load(open(r"C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\heart_model.pkl",'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\parkinson_model.pkl", 'rb'))


# loading the scalers

hearscale=pickle.load(open(r'C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\hearscale.pkl','rb'))

parkscale=pickle.load(open(r'C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\parkscale.pkl','rb'))

diabscale=pickle.load(open(r'C:\Users\nikso\OneDrive\Desktop\mlproject\Multiple Disease System\diabscale.pkl','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Check if you have Diabetes',
                           'Check if you have Heart Disease',
                           'Check if you have Parkinsons'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Check if you have Diabetes'):
    
    # page title
    st.title('Diabetes Report')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(diabscale.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]))
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'You have Diabetes.'
        else:
          diab_diagnosis = 'Congratulations!! You do not have Diabetes'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Check if you have Heart Disease'):
    
    # page title
    st.title('Heart Report')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        hr=hearscale.transform([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        heart_prediction = heart_disease_model.predict(hr)                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'You have symptoms of Heart diseases'
        else:
          heart_diagnosis = 'Congratulations!! You do not have any symptoms Heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Check if you have Parkinsons"):
    
    # page title
    st.title("Parkinson's Report")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
              
    with col5:
        Shimmer = st.text_input('MDVP:Shimmer')
              
    with col1:
        NHR = st.text_input('NHR')
        
    with col2:
        HNR = st.text_input('HNR')
        
    with col3:
        RPDE = st.text_input('RPDE')
        
    with col4:
        DFA = st.text_input('DFA')
        
    with col5:
        spread1 = st.text_input('spread1')
        
    with col1:
        spread2 = st.text_input('spread2')
        
    with col2:
        D2 = st.text_input('D2')
        
    with col3:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(parkscale.transform([[fo, fhi, flo, Jitter_percent,Shimmer,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]]))                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "You have symptoms of Parkinson's disease"
        else:
          parkinsons_diagnosis = "Congratulations!! You do not have any symptoms of Parkinson's disease"
        
    st.success(parkinsons_diagnosis)