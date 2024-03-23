import streamlit as st

def app():
	st.title("Welcome")
	choice=st.selectbox("Login/Signup",["Login","Signup"])
	if choice=="Login":
		email = st.text_input("User Name")
		password=st.text_input("Password",type="password")
		st.button("Login")
	else:
		fullname = st.text_input("Full Name")
		email = st.text_input("User Name")
		password=st.text_input("Password",type="password")
		confpass = st.text_input("Confirm Password", type="password")
		st.button("Signup")