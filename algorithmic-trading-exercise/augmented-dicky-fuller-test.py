# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 12:56:27 2017

@author: Jennifer
"""

from __future__ import print_function
# Import the Time Series library
import statsmodels.tsa.stattools as ts
from datetime import datetime
import pandas_datareader.data as web

stock = web.DataReader("AMZN", "google", datetime(2000,1,1), datetime.today())
# Output the results of the Augmented Dickey-Fuller test for Amazon
# with a lag order value of 1
adf = ts.adfuller(stock['Close'], 1)

print("the augmented Dick Fuller test results:")
print(adf)
if adf[0] > adf[4]['1%'] and adf[0] > adf[4]['5%'] and adf[0] > adf[4]['10%']:
    print("The null hypothesis is rejected. The tested time series is unlikely a meaning reverting time series.")