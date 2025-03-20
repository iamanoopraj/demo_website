import streamlit as st


name = st.text_input("Enter Your Name : ")
Fname = st.text_input("Enter Your Father Name : ")
Adress = st.text_area("Enter Your Adress : ")
Qualification = st.selectbox("Enter Your Qualification : ",("Selected","Fresher","Graduated","Post Graduate"))
button = (st.button("Submit"))
if button:
    st.markdown(f"""
    Name: {name}
    Father: {Fname}
    Adress: {Adress}
    Qualification: {Qualification}""")
    

