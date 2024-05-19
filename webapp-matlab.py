# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-5-19
# awake late night and connecting webinterfaces for matlab

#! usr/bin/python3 
# a web application to connect the matlab to web interface for the gene models 

import streamlit as st
import os
import pandas as pd
import math
import matlab.engine
st.set_page_config(
                 page_title="Matlab Web Interface",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width = 100)
st.header("Matlab webinterface")
st.subheader("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam, Germany", )
namedir = st.text_input("please enter the name of the directory")
workdir = st.text_input("please enter the name of the working directory")
click = st.button("makedirectory")
if click:
    os.chdir("namedir")
    os.mkdir("workdir")
fileupload = st.file_uploader("please upload the file for the gene expression")
if fileupload is not None:
   st.write(fileupload)
   fileinput = pd.read_csv(fileupload, sep = ",")
   st.dataframe(fileinput)
   edited_df = st.data_editor(fileinput)
   columns = st.multiselect("please select the names of the expression", fileinput.columns)
   maxvalue = edited_df[columns].max()
   selectcol = edited_df[columns]  
   st.write(maxvalue)
eng = matlab.engine.start_matlab()
logtransformed = eng.expressionormalize(selectcol)
engclick = st.button("give me the normalized values")
if engclick:
  st.write(f"The normalized values are {logtransformed}") 
