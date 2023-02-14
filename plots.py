# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 03:03:33 2023

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt


import seaborn as sns
import streamlit as st


data = pd.read_csv("gapminder_with_codes.csv")


st.subheader("Violin plot for population")
sns.violinplot(x=data["pop"])
st.pyplot()

st.subheader("Violin plot for GDP per cap")
sns.violinplot(x=data["gdpPercap"])
st.pyplot()

st.subheader("Violin plot for life expentancy ")
sns.violinplot(x=data["lifeExp"])
st.pyplot()










