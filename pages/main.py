import streamlit as st

from streamlit_option_menu import option_menu

import pages.1_Home as home,pages.account as account,pages.3_User_List as userlist,pages.about as about,pages.trending as trending,Login


st.set_page_config(
    page_title= "Spineac ERP"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title="Spineac ERP",
                options=["Home","Account","userdata","Trending","Your Posts","About"],
                icons=["house-fill","person-circle","trophy-fill","chat-fill","info-circle-fill"],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "userdata":
            userdata.app()
        if app == "Trending":
            trending.app()        
        if app == "Your Posts":
            Login.app()
        if app == "About":
            about.app()    
            
             
    run()            
         