import pandas as pd
import os 
import matplotlib.pyplot as plt
#data = pd.read_csv("Credit.csv")
data = pd.read_csv("Credit.csv", index_col=0, parse_dates=True)

data.plot()
plt.show(block=True)
#Prints the full data of the excel


#Prints the just the amount for the credit card 
#print (data["Amount"])





