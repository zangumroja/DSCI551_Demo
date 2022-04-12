'''import pandas as pd
import streamlit as st 
import sqlite3

crimes_data = pd.read_csv('USCcrimes.csv', encoding='latin1')
crimes_data.fillna('N/A', inplace=True)
crimes_data.replace(to_replace =["Date"], 
                            value ="To_Date")


conn = sqlite3.connect("data_incident.db")
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS incident_table(Alert_index TEXT, Crime TEXT,To_Date DATE,Weekday TEXT, Location TEXT)')

def add_data(Alert_index, Crime, To_Date, Weekday, Location):
	c.execute('INSERT INTO incident_table(Alert_index, Crime, To_Date, Weekday, Location) VALUES (?,?,?,?,?)', (Alert_index, Crime, To_Date, Weekday, Location))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM incident_table')
	data = c.fetchall()
	return data

def main():
	create = create_table()
	result = view_all_notes()

if __name__ == '__main__':
	main()
'''
import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from incident_data;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

