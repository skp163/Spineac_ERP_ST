import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)
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

