import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('userdata.db', check_same_thread=False)
c = conn.cursor()

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def app():
    st.title("User List")
    user_result = view_all_users()
    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
    st.dataframe(clean_db)


def main():
    st.title("User List")
    user_result = view_all_users()
    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
    st.dataframe(clean_db)

if __name__ == '__main__':
	main()