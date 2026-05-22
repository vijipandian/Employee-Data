import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as px
%matplotlib inline


data=pd.read_csv("/content/Employee Dataset (1).csv")
data.head(2)

data.info()
data.duplicated().sum()
data.isnull().sum()


fig,ax=plt.subplots(figsize=(6,5))
sns.barplot(data=data,x="age",y="salary",palette="Set2",hue="age",ax=ax)
st.title("age VS Salary")
st.pyplot(fig)


fig,ax=plt.subplots(figsize=(6,5))
sns.barplot(data=data,x="groups",y="healthy_eating",palette="Set1",hue="groups",ax=ax)
st.title("Healthy Eating by Groups")
st.pyplot(fig)



corr=data[["age","healthy_eating","active_lifestyle","salary"]].corr()
fig,ax=plt.subplots(figsize=(6,5))
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f",ax=ax)
st.title("Correlation Heatmap")
st.pyplot(fig)



pair_fig=sns.pairplot(data,vars=["age","healthy_eating","active_lifestyle","salary"],hue="groups")
st.pyplot(pair_fig.fig)


fig,ax=plt.subplots(figsize=(5,6))
sns.scatterplot(data=data,x="age",y="active_lifestyle",color="purple",ax=ax)
st.title("age vs activelifestyle")
st.pyplot(fig)
