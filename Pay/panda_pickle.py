import pandas as pd
import sqlite3, pickle

conn = sqlite3.connect('wages.db')

df = pd.read_sql_query("SELECT * FROM counties", conn)

print(df)