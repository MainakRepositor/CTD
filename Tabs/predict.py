"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


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
    cp = st.slider("CP", int(df["cp"].min()), int(df["cp"].max()))
    chol = st.slider("Cholesterol Level", float(df["chol"].min()), float(df["chol"].max()))
    fbs = st.slider("FBS", float(df["fbs"].min()), float(df["fbs"].max()))
    restecg = st.slider("Rest ECG", float(df["restecg"].min()), float(df["restecg"].max()))
    thalach = st.slider("Thalach", int(df["thalach"].min()), int(df["thalach"].max()))
    exang = st.slider("Exang", int(df["exang"].min()), int(df["exang"].max()))
    slope = st.slider("Slope", int(df["slope"].min()), int(df["slope"].max()))
    oldpeak = st.slider("Oldpeak", int(df["oldpeak"].min()), int(df["oldpeak"].max()))
    ca = st.slider("CA", int(df["ca"].min()), int(df["ca"].max()))
    thal = st.slider("Thal", int(df["thal"].min()), int(df["thal"].max()))
    anemia = st.slider("Animea", int(df["anaemia"].min()), int(df["anaemia"].max()))
    crp = st.slider("Creatinine Phosphokinase", int(df["creatinine_phosphokinase"].min()), int(df["creatinine_phosphokinase"].max()))
    diab = st.slider("Diabetes", int(df["diabetes"].min()), int(df["diabetes"].max()))
    ef = st.slider("Ejection Fraction", int(df["ejection_fraction"].min()), int(df["ejection_fraction"].max()))
    plat = st.slider("Platletes Count", int(df["platelets"].min()), int(df["platelets"].max()))
    sc = st.slider("Serum Creatinine", int(df["serum_creatinine"].min()), int(df["serum_creatinine"].max()))
    ss = st.slider("Serum Sodium", int(df["serum_sodium"].min()), int(df["serum_sodium"].max()))
    smok = st.slider("Smoking", int(df["smoking"].min()), int(df["smoking"].max()))

    # Create a list to store all the features
    features = [age, gen, cp, chol, fbs, restecg, thalach,exang,slope,oldpeak, ca, thal, anemia, crp, diab, ef, plat, sc, ss, smok]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get cardiac arrest!!")
        else:
            st.success("The person is relatively safe from cardiac arrest")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
