import streamlit as st
import pandas as pd

st.write("""
# Largest Number Finder App

Find the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_num = st.number_input("FIRST_NUM", value=0)
    second_num = st.number_input("SECOND_NUM", value=0)
    third_num = st.number_input("THIRD_NUM", value=0)

    data = {
            'FIRST_NUM': first_num,
            'SECOND_NUM': second_num,
            'THIRD_NUM': third_num,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

st.subheader('Result')
if df["FIRST_NUM"][0] >= df["SECOND_NUM"][0] and df["FIRST_NUM"][0] >= df["THIRD_NUM"][0]:
  st.write("The largest number is: ", df["FIRST_NUM"][0])
elif df["SECOND_NUM"][0] >= df["FIRST_NUM"][0] and df["SECOND_NUM"][0] >= df["THIRD_NUM"][0]:
  st.write("The largest number is: ", df["SECOND_NUM"][0])
elif df["THIRD_NUM"][0] >= df["FIRST_NUM"][0] and df["THIRD_NUM"][0] >= df["SECOND_NUM"][0]:
  st.write("The largest number is: ", df["THIRD_NUM"][0])