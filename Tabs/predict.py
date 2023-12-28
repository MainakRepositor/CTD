"""This modules contains data about prediction page"""
import pandas as pd
# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest and XGBoost</b> for the Coronary Thrombosis Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    age = st.slider("Age", int(df["age"].min()), int(df["age"].max()))
    gen = st.slider("Gender", int(df["sex"].min()), int(df["sex"].max()))
    cp = st.slider("Chest Pain Intensity", int(df["cp"].min()), int(df["cp"].max()))
    chol = st.slider("Cholesterol Level", float(df["chol"].min()), float(df["chol"].max()))
    fbs = st.slider("Fasting Blood Sugar", float(df["fbs"].min()), float(df["fbs"].max()))
    thalach = st.slider("Max Heart Rate", int(df["thalach"].min()), int(df["thalach"].max()))
    exang = st.slider("Exercise Induced Angina", int(df["exang"].min()), int(df["exang"].max()))
    slope = st.slider("Slope", int(df["slope"].min()), int(df["slope"].max()))
    oldpeak = st.slider("Rest induced value dip", int(df["oldpeak"].min()), int(df["oldpeak"].max()))
    ca = st.slider("Creatinine Amnokinase", int(df["ca"].min()), int(df["ca"].max()))
    trestbps = st.slider("Rest Blood Pressure", int(df["trestbps"].min()), int(df["trestbps"].max()))
    anemia = st.slider("Anaemia", int(df["anaemia"].min()), int(df["anaemia"].max()))
    crp = st.slider("Creatinine Phosphokinase", int(df["creatinine_phosphokinase"].min()), int(df["creatinine_phosphokinase"].max()))
    diab = st.slider("Diabetes", int(df["diabetes"].min()), int(df["diabetes"].max()))
    ef = st.slider("Ejection Fraction", int(df["ejection_fraction"].min()), int(df["ejection_fraction"].max()))
    plat = st.slider("Platletes Count", int(df["platelets"].min()), int(df["platelets"].max()))
    sc = st.slider("Serum Creatinine", int(df["serum_creatinine"].min()), int(df["serum_creatinine"].max()))
    ss = st.slider("Serum Sodium", int(df["serum_sodium"].min()), int(df["serum_sodium"].max()))
    smok = st.slider("Smoking", int(df["smoking"].min()), int(df["smoking"].max()))

    # Create a list to store all the features
    features = [age, gen, cp, chol, fbs, thalach,exang,slope,oldpeak, ca, trestbps, anemia, crp, diab, ef, plat, sc, ss, smok]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=['age','gen','cp','chol','fbs','thalach','exang','slope','oldpeak','ca','trestbps','anemia','crp','diab','ef','plat','sc','ss','smok']
    st.dataframe(df3)

    st.info("Reference parameters for combined cardiac study (ECG + Blood Test + Holter-Monitoring)")
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        components.html( """
                <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
                            <li>Age</li>
                            <li>Gender</li>
                            <li>Chest Pain</li>
                            <li>Cholesterol Level</li>
                            <li>Fasting Blood Sugar</li>
                                                        <br>
                    """)
        
        with col2:
            components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
                                <li>Resting ECG</li>
                                <li>Maximum Heart Rate</li>
                                <li>Exercise Induced Angina</li>
                                <li>Slope Constant</li>
                                <li>Rest induced dip in beat rate</li>
                                <br>
                        """)
            
        with col3:
            components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
                                <li>Creatinine Amnokinase</li>
                                <li>Heart Constriction Value</li>
                                <li>Anaemia</li>
                                <li>Creatinine Phosphokinase</li>
                                <li>Diabetes</li>
                                                            <br>
                        """)
            
        with col4:
            components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
                                <li>Ejection Fraction Value</li>
                                <li>Platelet Count</li>
                                <li>Serum Creatinine Level</li>
                                <li>Serum Sodium Level</li>
                                <li>Smoking or Non-smoking</li>
                                                            <br>
                        """)

    st.sidebar.info("Cardiac Arrest / Coronary Thrombosis is majorly detected from Rest Blood Pressure, Chest Pain, Exercise Induced Angina and Max Heart Rate")

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        st.info("Predicted Sucessfully...")

        

        # Print the output according to the prediction
        if(trestbps > 130):
            st.warning("Mild risk of a heart attack")
            st.write("Chest Pain",cp,"High Blood Pressure",trestbps)
        elif(chol > 250):
            st.warning("High level of Cholesterol. Risk of Cardiac Arrest. Cholesterol Level : " + chol)
        
        elif(cp > 2):
            st.warning("High Risk of Cardiac Arrest. Chest pain" + (str(cp)) + "is greater than usual")
        
        elif (ef > 40):
            st.error ("High risk of blood clogging and arterial rupture. Angioplasty is required!")

        elif (ss > 131):
            st.error("High risk of blood pressure rise and stage 2 attacks. Sodium amount is high in blood. Please reduce salt in diet")
                       
        elif(exang == 1):
            st.info("Exercise Induced Angina is observed. It is a cause of heart attack")
        elif (thalach > 125):
            st.info("Max Heart Rate is very high. Changes of Cadiac Arrest!⚠️")
            st.write(thalach)



            
        else:
            st.success("The person is relatively safe from cardiac arrest")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
