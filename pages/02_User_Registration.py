import streamlit as st
import pandas as pd
import hashlib
import mysql.connector


# Security
#passlib,hashlib,bcrypt,scrypt
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# DB Management
conn = mysql.connector.connect(
	host = "localhost",
	user = "admin",
	password = "Sunilkp@163",
	database="SpineacErp"
)
c = conn.cursor()

# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(fullname VARCHAR(255), department VARCHAR(255), role VARCHAR(255), mobile VARCHAR(255), username VARCHAR(255),password TEXT, PRIMARY KEY (username,mobile))')


def add_userdata(fullname, department, role, mobile, username,password):
	c.execute('INSERT INTO userstable(fullname, department, role, mobile, username,password) VALUES (%s,%s,%s,%s,%s,%s)',(fullname, department, role, mobile, username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def main():
	st.title("User Registration")
	fullname = st.text_input("Full Name")
	department = st.selectbox("Department",["Sourcing","Supply Chain","Wearhouse","Listing","Marketing and Sales","Finance"])
	role = st.selectbox("Role",["Employee","Manager"])
	mobile = st.text_input("Mobile Number With Country Code")
	new_user = st.text_input("Email")
	new_password=st.text_input("Password",type="password")
	confpass = st.text_input("Confirm Password", type="password")
	if st.button("Signup"):
		#Data input validation
			if fullname == "":
				st.error("Invalid Name")
				st.stop()
			elif department == "":
				st.error("Invalid Department")
				st.stop()
			elif role == "":
				st.error("Invalid Role")
				st.stop()
			elif mobile == "":
				st.error("Invalid Mobile Number")
				st.stop()
			elif new_user == "":
				st.error("Invalid Email")
				st.stop()
			elif new_password == "":
				st.error("Invalid Password")
				st.stop()
			elif confpass == "":
				st.error("Invalid Confirm Password")
				st.stop()
			elif new_password != confpass:
				st.error("Password and Confirm password mismatch")
				st.stop()
			else:
				create_usertable()
				add_userdata(fullname, department, role, mobile, new_user, make_hashes(new_password))
				st.success("You have successfully created a valid Account")
				st.info("Go to Login Menu to login")
				
if __name__ == '__main__':
	main()