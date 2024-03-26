import streamlit as st
import hashlib
import sqlite3
from st_pages import hide_pages
from time import sleep

# Security
#passlib,hashlib,bcrypt,scrypt
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
conn = sqlite3.connect('userdata.db', check_same_thread=False)
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

#Session state/hide functionalities for login
def log_in():
    st.session_state["logged_in"] = True
    hide_pages([])
    st.success("Logged in!")
    sleep(0.5)
    st.switch_page("pages/page1.py")
	
#Session state/hide functionalities for login
def log_out():
    st.session_state["logged_in"] = False
    st.success("Logged out!")
    sleep(0.5)
	


def main():
	if not st.session_state.get("logged_in", False):
		hide_pages(["about", "home", "trending","account","main","test","userdata","User_Registration"])
		choice=st.selectbox("Login/Forgot Password",["Login","Forgot-Password"])
		if choice == "Login":
			username = st.text_input("User Name")
			password=st.text_input("Password",type="password")
			if st.button("Login"):
				create_usertable()
				hashed_pswd = make_hashes(password)
				result = login_user(username,check_hashes(password,hashed_pswd))
				if result:
					st.success("Logged In as {}".format(username))
					st.session_state["logged_in"] = True
					hide_pages([])
					sleep(0.5)
					st.switch_page("pages/userdata.py")
				else:
					st.warning("Incorrect Username/Password")
	else:
		st.write("Logged in!")
		st.button("log out", on_click=log_out)


if __name__ == '__main__':
	main()