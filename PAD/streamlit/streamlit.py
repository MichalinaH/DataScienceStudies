import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

page = st.sidebar.selectbox('Select page',['Ankieta','Staty'])
    
if page == 'Ankieta':
    #Ankieta
    
    firstname = st.text_input("Please, enter your name", "Type here...")
    if st.button("Submit Name"):
        result = firstname.title()
        st.success("Questionnaire was saved correctly", icon="✅")
    
    surname = st.text_input("Please, enter your surname", "Type here...")
    if st.button("Submit Surname"):
        result = surname.title()
        st.success("Questionnaire was saved correctly", icon="✅")

    
else:
    #Staty
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        #progress bar
        import time
        my_bar = st.progress(0)
        
        for p in range(100):
            time.sleep(0.01)
            my_bar.progress(p + 1)
        st.success("Finished!")
        df = pd.read_csv(data)
        df = df[1:100]
        df = df.iloc[: , :7]
        df = df.drop_duplicates()
        df = df.dropna()
        st.dataframe(df.head(10))

        
        plot = st.selectbox("Select plot", ("Linear", "Bar"))
        st.write("You selected this plot: ", plot)
        
        if plot == "Linear":
            #Linear Time from Start to Finish (seconds)
            df = df.set_index('Time from Start to Finish (seconds)')
            df = df.sort_index()
            st.line_chart(df['Q5'])

        else:
            #Bar
            col1,col2 = st.columns(2)
            fig = px.line(df, 
		        x = "Q1", y = "Q2",
		        title = "Age per Gender",color = 'Q1')
            col1.plotly_chart(fig)
            