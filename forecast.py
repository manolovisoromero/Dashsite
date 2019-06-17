# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:14:43 2019

@author: manolo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries 
import seaborn as sns


##poverty lines
x_data = [
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015],
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015],
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015]
]

xd = [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013,2014, 2015]


y_data = [
    [2572, 2709, 2774, 3026, 2999, 3057, 2960, 2751, 2594, 2442, 2299, 2222, 2070, 1929],
    [2990, 3183, 3341, 3776, 3908, 4039, 4024, 3939, 3828, 3738, 3663, 3603, 3498, 3384],
    [1903, 1868, 1773, 1884, 1706, 1729, 1600, 1350, 1229, 1091, 962, 907, 802, 731]]

yd = [2572, 2709, 2774, 3026, 2999, 3057, 2960, 2751, 2594, 2442, 2299, 2222, 2070, 2005, 1929]

xd = np.array(x_data[2][3:13]).reshape(-1,1)
yd = np.array(y_data[2][3:13])


from sklearn.linear_model import LinearRegression


predictyears= [2018,2020,2023,2026,2029,2032,2035,2039,2042,2045]

for i in range(len(x_data)):
    xd = np.array(x_data[i][3:13]).reshape(-1,1)
    yd = np.array(y_data[i][3:13])
    model = LinearRegression()
    model.fit(xd, yd)
    X_predict = np.array(predictyears).reshape(-1,1)
    y_predict = model.predict(X_predict)
    for j in range(len(y_predict)):
        y_data[i].append(y_predict[j])
        x_data[i].append(predictyears[j])
        

for i in range(len(x_data)):
    print(x_data[i])    
    print(y_data[i])
        



##China prediction
trace1 = [
  [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], 
  [89.52054, 75.80584, 70.90941, 74.31364, 85.49856, 98.48678, 104.3246, 96.58953, 91.47272, 100.1299, 113.163, 118.6546, 131.8836, 157.0904, 160.1401, 178.3418, 165.4055, 185.4228, 156.3964, 183.9832, 194.8047, 197.0715, 203.3349, 225.4319, 250.714, 294.4588, 281.9281, 251.812, 283.5377, 310.8819, 317.8847, 333.1421, 366.4607, 377.3898, 473.4923, 609.6567, 709.4138, 781.7442, 828.5805, 873.2871, 959.3725, 1053.108, 1148.508, 1288.643, 1508.668, 1753.418, 2099.229, 2695.366, 3471.248, 3838.434, 4560.513, 5633.796, 6337.883, 7077.771, 7683.503, 8069.213, 8117.267, 8826.994] 
]


predictyears= [2018,2020,2023,2026,2029,2032,2035,2039,2042,2045]


xd = np.array(trace1[0][27:len(trace1[0])-1]).reshape(-1,1)    
yd = np.array(trace1[1][27:len(trace1[0])-1])
model = LinearRegression()
model.fit(xd, yd)
X_predict = np.array(predictyears).reshape(-1,1)
y_predict = model.predict(X_predict)
for j in range(len(y_predict)):
    trace1[1].append(y_predict[j])
    trace1[0].append(predictyears[j])
        
  
print("Expected Chinese GDP in 2040",trace1[1][len(trace1[1])-1])

