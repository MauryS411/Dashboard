import pandas as pd  
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="GIP Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded",
    )

# ---- READ EXCEL ACTIVA ----
@st.cache
def get_activa_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=100,
        header=2
    )

    # filter row on column value
    activa = ["VASTE ACTIVA","VLOTTENDE ACTIVA"]
    df = df[df['ACTIVA'].isin(activa)]

    return df

df_activa = get_activa_from_excel()
df_activa = df_activa.round({"Boekjaar 1":2, "Boekjaar 2":2, "Boekjaar 3":2})
st.write(df_activa)

#@st.cache
def get_rev_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
        engine="openpyxl",
        sheet_name="REV",
        usecols="A:D",
        nrows=10,
        header=1
    )
    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    rev = ["REV","RTV"]
    df = df[df["Type"].isin(rev)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","REV","RTV"] # change column names
    
    
    return df




df_rev = get_rev_from_excel()
st.write(df_rev)

fig = px.line(df_rev, x="Boekjaar", y=["REV","RTV"], markers=True)
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)



