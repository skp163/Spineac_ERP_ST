import streamlit as st
import pandas as pd
import hashlib
import sqlite3

#Gide: https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/

# Security
#passlib,hashlib,bcrypt,scrypt
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def app():
	st.title("Welcome")
	choice=st.selectbox("Login/Signup",["Login","Signup"])
	if choice=="Login":
		username = st.text_input("User Name")
		password=st.text_input("Password",type="password")
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
			else:
				st.warning("Incorrect Username/Password")
	else:
		fullname = st.text_input("Full Name")
		new_user = st.text_input("Eamil")
		new_password=st.text_input("Password",type="password")
		confpass = st.text_input("Confirm Password", type="password")
		if st.button("Signup"):
			if fullname == "":
				st.error("Invalid Name")
				st.stop
			elif  new_user == "":
				st.error("Invalid Email")
				st.stop
			elif new_password == "":
				st.error("Invalid Password")
				st.stop
			elif confpass == "":
				st.error("Invalid Confirm Password")
				st.stop
			elif new_password != confpass:
				st.error("Confirm password and password mismatch")
				st.stop
			else:
				create_usertable()
				add_userdata(new_user,make_hashes(new_password))
				st.success("You have successfully created a valid Account")
				st.info("Go to Login Menu to login")
		