import streamlit as st
import pandas as pd
import mysql.connector
from sqlite3 import Error


conn = mysql.connector.connect(
	host = "localhost",
	user = "admin",
	password = "Sunilkp@163",
	database="SpineacErp"
)
c = conn.cursor()

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def app():
    st.title("User List")
    user_result = view_all_users()
    clean_db = pd.DataFrame(user_result,columns=["fullname", "department", "role", "mobile","Username","Password"])
    st.dataframe(clean_db)


def main():
    st.title("User List")
    user_result = view_all_users()
    clean_db = pd.DataFrame(user_result,columns=["fullname", "department", "role", "mobile","Username","Password"])
    st.dataframe(clean_db)

if __name__ == '__main__':
	main()