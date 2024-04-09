import aspose.cells
from aspose.cells import Workbook
import pandas as pd
import mysql.connector
import datetime

'''

# --------------------------------------------------------------------------------------------------
# CSV to SQL
def csv_sql(f):
    workbook = Workbook()
    workbook.save(str(f).replace('.csv', '.sql'))


# Convertisseur
csv_sql("Data/xrpusd.csv")

# -----------------------------------------------------------------------------------------------------

'''


# Convertir le temps en secondes en date
def sdate(s):
    timestamp_in_s = s / 1000.0  # Convert to seconds
    date = datetime.datetime.fromtimestamp(timestamp_in_s)

    return date


# -----------------------------------------------------------------------------------------------------


# Database connection details
dbname = "crypto"
dbuser = "root"
dbpassword = ""
dbhost = "127.0.0.1"  # Or the host of your database server
dbport = 3306  # The port number of your MySQL server

# Connect to the database
conn = mysql.connector.connect(database=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)
cur = conn.cursor()
# REQUETES

# Colonne (time        open       close        high         low        volume)

# a) Get all data for a specific cryptocurrency
symbol = "BTC"
query = f"SELECT * FROM btcusd WHERE volume >0 ;"
cur.execute(query)
data = cur.fetchall()  # Fetch all results as a list of tuples
df = pd.DataFrame(data, columns=[col[0] for col in cur.description])  # Create DataFrame from results
print(df.to_string())  # Print the DataFrame

# b) Find the highest closing price for Bitcoin in the last year
date_query = "DATE_SUB(CURDATE(), INTERVAL 1 YEAR)"
query = f"SELECT MAX(close) AS highest_price FROM btcusd WHERE  time >= 157992453;"
cur.execute(query)
highest_price = cur.fetchone()[0]  # Fetch the first row (single value)
print(f"Highest closing price for BTC in the last year: {highest_price}")

# c) Calculate the average market capitalization for all cryptocurrencies on a specific date
date = "2024-04-09"
query = f"SELECT AVG(volume) AS vol FROM btcusd WHERE time = 15478936584;"
cur.execute(query)
vol = cur.fetchone()[0]
print(f"Average market capitalization on {sdate(15478936584)}: {vol}")

# d) Identify the top 5 cryptocurrencies by market capitalization
query = "SELECT open, close, volume FROM btcusd ORDER BY volume  DESC LIMIT 5;"
cur.execute(query)
top_5_data = cur.fetchall()
df = pd.DataFrame(top_5_data, columns=[col[0] for col in cur.description])
print(df.to_string())

# e) Track price changes over time for a specific cryptocurrency
symbol = "BTC"
query = f"SELECT time, high FROM btcusd WHERE volume <= '{5000}' ORDER BY time ASC;"
cur.execute(query)
price_changes = cur.fetchall()
print("Date\tPrice")
for row in price_changes:
    print(f"{row[0]}\t{row[1]}")

# Close the connection
cur.close()
conn.close()
