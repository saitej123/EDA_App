import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components


st.set_page_config(layout = "wide")
st.markdown(
    """
    <style> [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 220px; }[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 140px; margin-left: -140px; }.css-qrbaxs, .streamlit-expanderHeader{font-size: 8px
    } body { color: #fff;background-color: #4F8BF9;} </style>  """,
    unsafe_allow_html=True,
)

#the title of the web app
html_temp = """
    <div style="background-color:rebeccapurple;"><p style="color:white;font-size:50px;padding:10px">Jupyter Note Book </p></div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

notebook_file = open('./pages/notebook.html','r')
components.html(notebook_file.read(), height=18000, scrolling=True)





def main():
    st.sidebar.text(" ")
    pass

if __name__ == '__main__':
    main()

    # brief about the app
    st.sidebar.header("About App")
    st.sidebar.markdown("A Simple EDA App for full Analysis Dataset.")
    st.sidebar.markdown("Upload any dataset in CSV format, it will show the full analysis with visualization")
    st.sidebar.info("Developed By: \t \t \t Sai Teja")
