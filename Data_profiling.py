import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
import streamlit_pandas_profiling
from streamlit_pandas_profiling import st_profile_report
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
    <div style="background-color:rebeccapurple;"><p style="color:white;font-size:50px;padding:10px">Data Profiling</p></div>
    """

st.markdown(html_temp,unsafe_allow_html=True)

# Upload CSV data
st.subheader('Upload your CSV data')
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file,encoding = 'unicode_escape', engine ='python')
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df.head(6))
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')

check=st.checkbox("Load offline Profiling file")
if check:
    plot_file = open('./report.html','r')
    # plot = plot_file.read()
    # st.markdown(plot,unsafe_allow_html=True)
    # plot = plot_file.close()
    components.html(plot_file.read(), height=11800, scrolling=True)

 # brief about the app
def main():
    st.sidebar.text(" ")
    pass

if __name__ == '__main__':
    main()

    st.sidebar.text(" ")
    st.sidebar.header("About App")
    st.sidebar.markdown("A Simple EDA App for full Analysis Dataset.")
    st.sidebar.markdown("Upload any dataset in CSV format, it will show the full analysis with visualization")
    st.sidebar.info("Developed By: \t \t \t Sai Teja")