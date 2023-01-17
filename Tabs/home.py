"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Coronary Thrombosis Predictor")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Coronary Thrombosis is a chronic health emergency condition that affects how your heart pumps blood throughout your body.
            It is not a disease but a phenomena, where there are sudden cardiac arrests. Having healthy, low-cholesterol food, and being active can really help in reducing the chances of cardiac arrest.
            This Web app will help you to predict whether a person has chances of cardiac arrest or is prone to get it in future by analysing the values of several features using the Random Forest Classifier, Recurrent Neural Networks(RNN) and Xtreme Gradient Boosting.
        </p>
    """, unsafe_allow_html=True)