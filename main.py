import streamlit as st


st.title("Welcome to My first Website")

#Creating a form Using Streamlit

Name = st.text_input("Enter your name: ")
Fname = st.text_input("Enter your Father name: ")
Address= st.text_area("Enter your Current Address")
classdata = st.selectbox("Enter your class",(1,2,3,4,5,6))
button =st.button("submitt")

if button:
    st.markdown(f""" 
        Name : {Name}
        Father name : {Fname}
        Address : {Address}
        Classdata : {classdata}
    """)