import streamlit as st
import sqlite3


conn = sqlite3.connect('userdata.db', check_same_thread=False)
c = conn.cursor()

username  = st.text_input("Enter Username to delete: ")
def main():
    username  = st.text_input("Enter Username to delete: ")
	c.execute('DELETE from userstable where username = username')
	st.button("Delete")
	conn.commit()


if __name__ == '__main__':
	main()
