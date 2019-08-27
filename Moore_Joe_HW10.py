"""
************************************************************************
Description: This program will import a JSON file and then create a 
line graph that will display the stocks changing value. Then it will 
create a pie chart that will show the value distribution.

Author: Joe Moore

Last Revision: 8/27/19
************************************************************************
"""

import stock
import json
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

filePath = 'AllStocks.json' 
with open(filePath) as f:
    dataSet = json.load(f)


#Create dictionary to hold data
stockDictionary = {}
equityDic = {}
stockDic =[]
closeDic =[]
#Create Stock Dictionaries

for data in dataSet:
	
	if data['Symbol'] not in stockDictionary:
		newStock = stock.Stock(data['Symbol'], data['Date'], data['Close'])
		stockDictionary[data['Symbol']] = {'stock': newStock}
	stockDictionary[data['Symbol']]['stock'].addClose(data['Close'],datetime.strptime(data['Date'], '%d-%b-%y'))

#Create Stock Plot
for purchase in stockDictionary:
	close_price = stockDictionary[purchase]['stock'].stockClose
	dates = matplotlib.dates.date2num(stockDictionary[purchase]['stock'].dayStockClosed)
	name = stockDictionary[purchase]['stock'].Symbol
	plt.plot_date(dates, close_price, linestyle='solid', marker='None', label = name)

plt.legend()
plt.show()

for equity in dataSet:
	
	if equity['Symbol'] not in equityDic:
		stock = equity['Symbol']
		close = equity['Close']
		stockDic.append(stock)
		closeDic.append(close)
		equityDic[equity['Symbol']] = close


labels = stockDic
sizes = closeDic	


plt.pie(sizes,labels=labels, startangle=90, autopct='%1.1f%%')

plt.axis('equal')

plt.show()


