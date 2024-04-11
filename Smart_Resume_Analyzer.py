import streamlit as st
import pandas as pd
import base64, random 
import time,datetime
from pyresparser import ResumeParser 
from pdfminer3.layout import LAParams, LLTestBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io,random
from streamlit_tags import st_tags
from PIL import Image
import pymysql
from Courses import ds_course,web_courses,android_course,ios_course,uiux_course
import pafy 
import plotly.express as px 


connection = pymysql.connect(host='localhost',user='root',password='',db='sra')
cursor = connection.cursor()

st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon='./Logo/SRA_Logo.ico',
)


def run():
    st.title("Smart Resume Analyser")
    st.sidebar.markdown("# Choose User")
    activities = ["Normal User","Admin"]
    choice = st.sidebar.selectbox("Choose among the give options",activities)
    img = Image.open("")      # Logo path
    img = img.resize((250,250))
    st.image(img)

    #create the DATABASE

    db_sql = """CREATE DATABASE IF NOT EXISTS SRA"""
    cursor.execute(db_sql)

    #Create Table
    DB_table_name = 'user_data'
    table_sql = "CREATE TABLE IF NOT EXISTS" + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                    Name VARCHAR(100) NOT NULL,
                    Email_ID VARCHAR(50) NOT NULL,
                    Timestamp VARCHAR(50) NOT NULL,
                    Page_no VARCHAR(5) NOT NULL,
                    Predicted_Field VARCHAR(25) NOT NULL,
                    User_level VARCHAR(30) NOT NULL,
                    Actual_skills VARCHAR(300) NOT NULL,
                    Recommended_skills VARCHAR(300) NOT NULL,
                    Recommended_courses VARCHAR(600) NOT NULL,
                    PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)
    if choice == 'Normal User':
        #st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Upload yoir resume
        #           unsafe_allow_html=True)
        pdf_file = st.file_uploader("choose Your Resume", type=["pdf"])
        if pdf_file is not None:
            # with st.spinner('Uploading Your Resume ...'):
            #   time.sleep(4)
            save_image_path = '/Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            if resume_data:
                resume_text = pdf_reader(save_image_path)




def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64decode(f.read()).decode('utf-8')
    pdf_display = 