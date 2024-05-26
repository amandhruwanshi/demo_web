import streamlit as st

st.header("Basic Information")
name = st.text_input("Enter you name")
fname =  st.text_input("Enter your father name")
add  = st.text_area("enter you text : ")
classdata = st.selectbox("Enter your class : ",(1,2,3,4,5,6,7,8,9,10))

button = st.button("CONFIRM")

if button:
    st.markdown(f"""
Name : {name}
Fname : {fname}
address : {add}
class : {classdata}
""")

