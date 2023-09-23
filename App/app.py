import streamlit as st
import pandas as pd
import os

#Import profile_report
import ydata_profiling as pp
from streamlit_pandas_profiling import st_profile_report

# Machine Learning
from pycaret.classification import setup, compare_models, pull, save_model

with st.sidebar:
    st.image("https://builtin.com/sites/www.builtin.com/files/styles/og/public/2021-12/machine-learning-examples-applications.png")
    st.title("Auto Machine Learning Model Generator")
    choice = st.radio("Navigation", ["Home", "Data Upload", "Profiling", "ML", "Download"])
    st.info("This is an application to help you with DNS Traffic Control with Machine Learning")

if os.path.exists("source.csv"):
    df = pd.read_csv("source.csv", index_col=None)

if choice == "Home":
  st.title("Welcome to AutoML Model Generator")
  st.write("Hello! This is a Machine Learning Model Generator. You can input your dataset and generate a Machine Learning Model. Also, you can download the model and use it for your own purpose. The model you are downloading is a pickle file, that contains the highest accuracy model selected by the AutoML. You can also access profiling report of your dataset and explore it.")
  st.write("Under the Data Upload tab you can upload your dataset. The dataset should be in .csv format. After uploading the dataset, you can access the profiling report of your dataset under the Profiling tab. You can also generate a Machine Learning Model under the ML tab and see all the models compared side by side with their respective scores. After generating the model, you can download it under the Download tab.")
  st.divider()

if choice == "Data Upload":
   st.title("Upload your dataset")
   file = st.file_uploader("Upload your dataset here")
   if file:
      df = pd.read_csv(file, index_col=None)
      df.to_csv("source.csv", index=None)
      st.dataframe(df)
      st.write("File uploaded successfully")


if choice == "Profiling":
    st.title("Exploratory Data Analysis")
    if st.button("Generate Report"):
        profile_report = df.profile_report()
        st_profile_report(profile_report)


if choice == "ML":
    st.title("Machine Learning Generator")
    target = st.selectbox("Select your target", df.columns)
    if st.button("Train"):
      setup(df, target=target)
      setup_df = pull()
      st.info("This is the ML Experiment")
      st.dataframe(setup_df)
      best_model = compare_models()
      compare_models_df = pull()
      st.info("This is the best model")
      save_model(best_model, "best_model")
      st.dataframe(compare_models_df)

if choice == "Download":
    with open("best_model.joblib", "rb") as f:
        st.download_button("Download the model", f, "trained_model.joblib")
