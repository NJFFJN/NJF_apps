import sqlite3
import requests
import streamlit as st

# URL to your raw SQLite file on GitHub
DB_URL = "https://github.com/your_username/your_repo/raw/main/aga.guide.database.db"

# Download the database and save it locally
@st.cache_data
def download_db():
    r = requests.get(DB_URL)
    open("aga.guide.database.db", "wb").write(r.content)

# Load database (will only download once)
download_db()
conn = sqlite3.connect("aga.guide.database.db")

# Query example: Fetch all data from a table
df = pd.read_sql("SELECT * FROM table_1", conn)
st.write(df.head())  # Show first 5 rows

conn.close()


st.title("🎈 My old app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
