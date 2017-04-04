#!/usr/bin/python
# -*- coding: utf-8 -*-

# retrieving_data.py

from __future__ import print_function
import sys
import pandas as pd
import MySQLdb as mdb


if __name__ == "__main__":
    try:
        ticker = sys.argv[1] 
    except IndexError:
        print('usage: python retrieving_data.py TICKER')
        sys.exit(1)
        
    # Connect to the MySQL instance
    db_host = 'localhost'
    db_user = 'sec_user'
    db_pass = 'password'
    db_name = 'securities_master'
    con = mdb.connect(db_host, db_user, db_pass, db_name)

    # Select all of the historic Google adjusted close data
    sql = """SELECT dp.price_date, dp.open_price, dp.high_price, dp.low_price, 
                    dp.close_price, dp.adj_close_price, dp.volume
             FROM symbol AS sym
             INNER JOIN daily_price AS dp
             ON dp.symbol_id = sym.id
             WHERE sym.ticker = '%s'
             ORDER BY dp.price_date ASC;""" % ticker

    # Create a pandas dataframe from the SQL query
    goog = pd.read_sql_query(sql, con=con, index_col='price_date')    

    # Output the dataframe tail
    print(goog.tail())
