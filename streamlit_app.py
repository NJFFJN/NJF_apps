import sqlite3
import requests
import pandas as pd
import streamlit as st

# URL to your raw SQLite file on GitHub
DB_URL = "https://github.com/NJFFJN/NJF_apps/blob/main/aga_guide_database.db"

# Download the database and save it locally
@st.cache_data
def download_db():
    r = requests.get(DB_URL)
    open("aga.guide.database.db", "wb").write(r.content)

# Load database (will only download once)
download_db()
conn = sqlite3.connect("aga.guide.database.db")

# Query the first 3 rows from the 'structure_database' table
query = "SELECT * FROM structure_database LIMIT 3"
df = pd.read_sql(query, conn)

# Show the first 3 rows in the Streamlit app
st.write("First 3 rows from 'structure_database':")
st.write(df)  # Display the dataframe

conn.close()


