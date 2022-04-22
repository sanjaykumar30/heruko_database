from turtle import st
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from postgres_connect import *

sql="select * from data_training_2.cars"
data=pd.DataFrame(runquery(sql))
data.columns=["name","miles_per_gallon","cylinders","displacement","horsepower","weight_in_lbs","acceleration","year","origin"]
st.title("CARS DATA SOURCED FROM - HERUKO")
st.table(data)