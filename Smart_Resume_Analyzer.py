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