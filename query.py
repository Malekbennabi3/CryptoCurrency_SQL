import pandas as pd
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


# Define your database connection parameters
db_username = "root"
db_password = ""
db_name = "crypto_bdd"
db_host = "127.0.0.1"

# Create the SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}/{db_name}")

# List of SQL query
#sql_query = "SELECT * FROM ada_usd,avax_usd,bnb_usd,btc_usd,dot_usd,eth_usd,link_usd,ltc_usd,shib_usd,sol_usd,steth_usd,usdc_usd,usdt_usd,wbtc_usd,xrp_usd ;";

#sql_query = "SELECT volume FROM ada_usd,avax_usd;";

#SQL JOIN
#sql_query="SELECT t1.date, t1.volume as volume_btc, t2.volume as volume_usdc FROM btc_usd as t1 JOIN usdc_usd as t2 ON t1.date  = t2.date;"

#Join volumes
#sql_query="SELECT t1.date,t1.volume as vol_ada,t2.volume as vol_avax,t3.volume as vol_bnb,t4.volume as vol_btc,t5.volume as vol_dot,t6.volume as vol_eth,t7.volume as vol_link,t8.volume as vol_ltc,t9.volume as vol_shib,t10.volume as vol_sol,t11.volume as vol_steth,t12.volume as vol_usdc,t13.volume as vol_usdt,t14.volume as vol_wbtc,t15.volume as vol_xrp "+" FROM ada_usd as t1 JOIN avax_usd as t2 ON t1.date = t2.date JOIN bnb_usd as t3 ON t1.date = t3.date "+" JOIN btc_usd as t4 ON t1.date = t4.date "+" JOIN dot_usd as t5 ON t1.date = t5.date "+" JOIN eth_usd as t6 ON t1.date = t6.date "+" JOIN link_usd as t7 ON t1.date = t7.date "+" JOIN ltc_usd as t8 ON t1.date = t8.date "+" JOIN shib_usd as t9 ON t1.date = t9.date "+" JOIN sol_usd as t10 ON t1.date = t10.date "+" JOIN steth_usd as t11 ON t1.date = t11.date"+" JOIN usdc_usd as t12 ON t1.date = t12.date "+" JOIN usdt_usd as t13 ON t1.date = t13.date"+" JOIN wbtc_usd as t14 ON t1.date = t14.date"+" JOIN xrp_usd as t15 ON t1.date = t15.date;"

#Join open
#sql_query="SELECT t1.date,t1.open as open_ada,t2.open as open_avax,t3.open as open_bnb,t4.open as open_btc,t5.open as open_dot,t6.open as open_eth,t7.open as open_link,t8.open as open_ltc,t9.open as open_shib,t10.open as open_sol,t11.open as open_steth,t12.open as open_usdc,t13.open as open_usdt,t14.open as open_wbtc,t15.open as open_xrp "+" FROM ada_usd as t1 JOIN avax_usd as t2 ON t1.date = t2.date JOIN bnb_usd as t3 ON t1.date = t3.date "+" JOIN btc_usd as t4 ON t1.date = t4.date "+" JOIN dot_usd as t5 ON t1.date = t5.date "+" JOIN eth_usd as t6 ON t1.date = t6.date "+" JOIN link_usd as t7 ON t1.date = t7.date "+" JOIN ltc_usd as t8 ON t1.date = t8.date "+" JOIN shib_usd as t9 ON t1.date = t9.date "+" JOIN sol_usd as t10 ON t1.date = t10.date "+" JOIN steth_usd as t11 ON t1.date = t11.date"+" JOIN usdc_usd as t12 ON t1.date = t12.date "+" JOIN usdt_usd as t13 ON t1.date = t13.date"+" JOIN wbtc_usd as t14 ON t1.date = t14.date"+" JOIN xrp_usd as t15 ON t1.date = t15.date;"

#Join close
#sql_query="SELECT t1.date,t1.close as close_ada,t2.close as close_avax,t3.close as close_bnb,t4.close as close_btc,t5.close as close_dot,t6.close as close_eth,t7.close as close_link,t8.close as close_ltc,t9.close as close_shib,t10.close as close_sol,t11.close as close_steth,t12.close as close_usdc,t13.close as close_usdt,t14.close as close_wbtc,t15.close as close_xrp "+" FROM ada_usd as t1 JOIN avax_usd as t2 ON t1.date = t2.date JOIN bnb_usd as t3 ON t1.date = t3.date "+" JOIN btc_usd as t4 ON t1.date = t4.date "+" JOIN dot_usd as t5 ON t1.date = t5.date "+" JOIN eth_usd as t6 ON t1.date = t6.date "+" JOIN link_usd as t7 ON t1.date = t7.date "+" JOIN ltc_usd as t8 ON t1.date = t8.date "+" JOIN shib_usd as t9 ON t1.date = t9.date "+" JOIN sol_usd as t10 ON t1.date = t10.date "+" JOIN steth_usd as t11 ON t1.date = t11.date"+" JOIN usdc_usd as t12 ON t1.date = t12.date "+" JOIN usdt_usd as t13 ON t1.date = t13.date"+" JOIN wbtc_usd as t14 ON t1.date = t14.date"+" JOIN xrp_usd as t15 ON t1.date = t15.date;"

#Join high
#sql_query="SELECT t1.date,t1.high as high_ada,t2.high as high_avax,t3.high as high_bnb,t4.high as high_btc,t5.high as high_dot,t6.high as high_eth,t7.high as high_link,t8.high as high_ltc,t9.high as high_shib,t10.high as high_sol,t11.high as high_steth,t12.high as high_usdc,t13.high as high_usdt,t14.high as high_wbtc,t15.high as high_xrp "+" FROM ada_usd as t1 JOIN avax_usd as t2 ON t1.date = t2.date JOIN bnb_usd as t3 ON t1.date = t3.date "+" JOIN btc_usd as t4 ON t1.date = t4.date "+" JOIN dot_usd as t5 ON t1.date = t5.date "+" JOIN eth_usd as t6 ON t1.date = t6.date "+" JOIN link_usd as t7 ON t1.date = t7.date "+" JOIN ltc_usd as t8 ON t1.date = t8.date "+" JOIN shib_usd as t9 ON t1.date = t9.date "+" JOIN sol_usd as t10 ON t1.date = t10.date "+" JOIN steth_usd as t11 ON t1.date = t11.date"+" JOIN usdc_usd as t12 ON t1.date = t12.date "+" JOIN usdt_usd as t13 ON t1.date = t13.date"+" JOIN wbtc_usd as t14 ON t1.date = t14.date"+" JOIN xrp_usd as t15 ON t1.date = t15.date;"

#Join low
sql_query="SELECT t1.date,t1.low as low_ada,t2.low as low_avax,t3.low as low_bnb,t4.low as low_btc,t5.low as low_dot,t6.low as low_eth,t7.low as low_link,t8.low as low_ltc,t9.low as low_shib,t10.low as low_sol,t11.low as low_steth,t12.low as low_usdc,t13.low as low_usdt,t14.low as low_wbtc,t15.low as low_xrp "+" FROM ada_usd as t1 JOIN avax_usd as t2 ON t1.date = t2.date JOIN bnb_usd as t3 ON t1.date = t3.date "+" JOIN btc_usd as t4 ON t1.date = t4.date "+" JOIN dot_usd as t5 ON t1.date = t5.date "+" JOIN eth_usd as t6 ON t1.date = t6.date "+" JOIN link_usd as t7 ON t1.date = t7.date "+" JOIN ltc_usd as t8 ON t1.date = t8.date "+" JOIN shib_usd as t9 ON t1.date = t9.date "+" JOIN sol_usd as t10 ON t1.date = t10.date "+" JOIN steth_usd as t11 ON t1.date = t11.date"+" JOIN usdc_usd as t12 ON t1.date = t12.date "+" JOIN usdt_usd as t13 ON t1.date = t13.date"+" JOIN wbtc_usd as t14 ON t1.date = t14.date"+" JOIN xrp_usd as t15 ON t1.date = t15.date;"





# Use pandas to execute the SQL query
df = pd.read_sql(sql_query, con=engine)

# Write the DataFrame to a CSV file
df.to_csv('lows.csv', index=False)
