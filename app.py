import pandas as pd  
import plotly.express as px
import streamlit as st
from PIL import Image

# -----Search bar----
st.set_page_config(
    page_title="Dashboard GIP", 
    layout="wide",
    initial_sidebar_state="expanded"
    )



# ---- SIDEBAR ----
st.sidebar.header("Selecteer pagina:")
ratios = st.sidebar.radio(label = "",
    options=("Home","Liquiditeit","Solvabiliteit","Rentabiliteit","Samenstelling activa en passiva","Voorraadrotatie"),
    index=0
)
if ratios == "Samenstelling activa en passiva":

    boekjaar = st.sidebar.radio(
        "Selecteer het boekjaar:",
        ("Boekjaar 1","Boekjaar 2","Boekjaar 3"),
        index=0
    )
if ratios == "Home":
    col1, col2, col3 = st.columns(3)
st.header("Welkom in de wondere wereld van Mylène!")
with col1:
    image=Image.open("data/logo.png")
    st.image(image,width=100)

with col2:
    image =Image.open("data/mylène.png")
    st.image(image,width=400)

with col3:
    
    
    
    

    
    




if ratios == "Liquiditeit":
    st.title("Ratio's Mylène")
#---- READ EXCEL LIQUIDITEIT ---
    def get_liq_from_excel():
        df = pd.read_excel(
            io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
            engine="openpyxl",
            sheet_name="Liquiditeit",
            usecols="A:D",
            nrows=32,
            header=1
        )
        # change column names
        df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
        # filter row on column value
        liq = ["LIQUIDITEIT IN RUIME ZIN","LIQUIDITEIT IN ENGE ZIN"]
        df = df[df["Type"].isin(liq)]

        df = df.T #Transponeren
        df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                        "Boekjaar 3":"3"})
        df = df.iloc[1: , :] # Drop first row 
        df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                        "Boekjaar 3"],True)
        df.columns = ["Boekjaar","Liquiditeit in ruime zin","Liquiditeit in enge zin"] # change column names
        
        
        return df

    df_liq = get_liq_from_excel()

    #Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='liquiditeit'):
        st.subheader('Liquiditeit')
        st.write(df_liq)

    fig_liq = px.line(df_liq, x="Boekjaar", y=["Liquiditeit in ruime zin","Liquiditeit in enge zin"], color_discrete_sequence = ["purple","pink"], markers=True)
    fig_liq.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig_liq.update_traces(line=dict(width=3))
    fig_liq.update_layout(title_text='Liquiditeit', title_x=0.5, xaxis_title= "Boekjaar", yaxis_title="Liquiditeit")
    st.plotly_chart(fig_liq, use_container_width=True)

#---- READ EXCEL SOLVABILITEIT ----
if ratios == "Solvabiliteit":
    st.title("Ratio's Mylène")

    def get_solv_from_excel():
        df = pd.read_excel(
            io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
            engine="openpyxl",
            sheet_name="Solvabiliteit",
            usecols="A:D",
            nrows=6,
            header=0
        )
        # change column names
        df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
        # filter row on column value
        solv = ["Solvabiliteit"]
        df = df[df["Type"].isin(solv)]

        df = df.T #Transponeren
        df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                        "Boekjaar 3":"3"})
        df = df.iloc[1: , :] # Eerste lijn weglaten
        df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                        "Boekjaar 3"],True)
        df.columns = ["Boekjaar","Solvabiliteit"] # kolom van naam veranderen
        
        
        return df

    df_solv = get_solv_from_excel()

    #Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='solvabiliteit'):
        st.subheader('Solvabiliteit')
        st.write(df_solv)

    fig_solv = px.line(df_solv, x="Boekjaar", y="Solvabiliteit", color_discrete_sequence = ["purple"], markers=True)
    fig_solv.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig_solv.update_traces(line=dict(width=3))
    fig_solv.update_layout(title_text='Solvabiliteit', title_x=0.5)
    st.plotly_chart(fig_solv, use_container_width=True)

#---- READ EXCEL RENTABLITEIT ----
if ratios == "Rentabiliteit":
    st.title("Ratio's Mylène")

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
        rev = ["REV"]
        df = df[df["Type"].isin(rev)]

        df = df.T #Transponeren
        df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                        "Boekjaar 3":"3"})
        df = df.iloc[1: , :] # Drop first row 
        df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                        "Boekjaar 3"],True)
        df.columns = ["Boekjaar","REV"] # change column names
        
        
        return df

    df_rev = get_rev_from_excel()

    #Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='rentabiliteit'):
        st.subheader('Rentabiliteit')
        st.write(df_rev)

    fig_rev = px.line(df_rev, x="Boekjaar", y="REV", color_discrete_sequence = ["purple"], markers=True)
    fig_rev.update_layout({
    'plot_bgcolor': 'rgb(0, 0, 0)',
    'paper_bgcolor': 'rgb(0, 0, 0)',})

    fig_rev.update_traces(line=dict(width=3))
    fig_rev.update_layout(title_text='Rentabiliteit van het EV', title_x=0.5)
    st.plotly_chart(fig_rev, use_container_width=True)

    # ---- READ EXCEL ACTIVA ----
if ratios == "Samenstelling activa en passiva":
    st.title("Ratio's Mylène")
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
        df.drop(df.columns[[1]], axis=1, inplace = True)

        # filter row on column value
        activa = ["VASTE ACTIVA","VLOTTENDE ACTIVA"]
        df = df[df['ACTIVA'].isin(activa)]
        df = df.astype({"Boekjaar 1": "float64","Boekjaar 2":"float64","Boekjaar 3":"float64"})
        return df

    df_activa = get_activa_from_excel()

    # Samenstelling activa boekjaar [TAART DIAGRAM]
    fig_activa = px.pie(df_activa, 
                values=boekjaar, 
                names='ACTIVA',
                title=f'Samenstelling activa {boekjaar}',
                color_discrete_sequence = ["#800080", "#ffc0cb "],        
                )
    fig_activa.update_layout({'plot_bgcolor': 'rgb(255, 255, 255)'})
    #'paper_bgcolor': 'rgb(0, 0, 0)'})

# ---- READ EXCEL PASIVA ---- 
    @st.cache
    def get_passiva_from_excel():
        df = pd.read_excel(
            io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
            engine="openpyxl",
            sheet_name="verticale analyse balans",
            usecols="A:E",
            nrows=100,
            header=50
        )
        df.drop(df.columns[[1]], axis=1, inplace = True)
        # filter row on column value
        passiva = ["EIGEN VERMOGEN","VOORZIENINGEN EN UITGESTELDE BELASTINGEN","SCHULDEN"]
        df = df[df['PASSIVA'].isin(passiva)]
        df = df.astype({"Boekjaar 1": "float64","Boekjaar 2":"float64","Boekjaar 3":"float64"})
        return df

    df_passiva = get_passiva_from_excel()
    
    # Samenstelling passiva boekjaar [TAART DIAGRAM]
    fig_passiva = px.pie(df_passiva, 
                values=boekjaar, 
                names='PASSIVA',
                title= f'Samenstelling passiva {boekjaar}',
                color_discrete_sequence = ["#800080", "#ffc0cb "],            
                )
    #fig_passiva.update_traces(textfont_size=20, pull=[0, 0.2], marker=dict(line=dict(color='#000000', width=2)))
    #fig_passiva.update_layout(legend = dict(font = dict(size = 20)), title = dict(font = dict(size = 30)))



    
        
#Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='activa'):
        st.subheader('Activa')
        st.write(df_activa)
    st.plotly_chart(fig_activa, use_container_width=True)
#Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='passiva'):
        st.subheader('Passiva')
        st.write(df_passiva)
    st.plotly_chart(fig_passiva, use_container_width=True)


#---- READ EXCEL VOORRAADROTATIE ----
if ratios == "Voorraadrotatie":
    st.title("Ratio's Mylène")
    
    def get_voorraad_from_excel():
        df = pd.read_excel(
            io="data/GIP_analyse van de jaarrekening_Maury.xlsx",
            engine="openpyxl",
            sheet_name="Voorraad",
            usecols="A:D",
            nrows=6,
            header=0
        )
        # change column names
        df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
        # filter row on column value
        voorraad = ["Omlooptijd"]
        df = df[df["Type"].isin(voorraad)]

        df = df.T #Transponeren
        df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                        "Boekjaar 3":"3"})
        df = df.iloc[1: , :] # Drop first row 
        df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                        "Boekjaar 3"],True)
        df.columns = ["Boekjaar","Voorraad"] # change column names
        
        
        return df

    df_voorraad = get_voorraad_from_excel()

    #Use a button to toggle data
    if st.checkbox('Toon de cijfers:', key='om_voorraad'):
        st.subheader('Voorraadrotatie')
        st.write(df_voorraad)

    fig_voorraad = px.bar(df_voorraad, x="Boekjaar", y="Voorraad")
    fig_voorraad.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig_voorraad.update_traces(width=0.40)
    fig_voorraad.update_layout(title_text='Omlooptijden van de voorraad', title_x=0.5)
    st.plotly_chart(fig_voorraad, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)