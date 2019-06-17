import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go
import dash_daq as daq


import pandas as pd
import numpy as np

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')




##START data source
df_pov = pd.read_csv("pov.csv", header=None, encoding='iso-8859-1', sep=',', low_memory=False)
povagr = pd.read_csv('aggregatedyears.csv')

#df_gdp = pd.read_csv("gdp.csv", header=None, encoding='iso-8859-1', sep=',', low_memory=False)
names = df_pov.iloc[0]
df_pov.rename(columns=names)
df_pov.columns = names

df_pov = (df_pov.loc[df_pov.iloc[:,3] == 'SI.POV.GAPS'] )
df_pov = df_pov.dropna(axis=1,how='all')
df_pov = df_pov.dropna(axis=0,how='all')
df_pov.rename(columns=names)
#df_pov.to_csv("out.csv", index=False)
df_pov = povagr
yearlist = []
countrylist = df_pov.iloc[:,0].values.tolist()
countrynames = df_pov.iloc[:,1].values.tolist()
length = len(df_pov.columns) 
i = 0
for column in  df_pov:
    if i > 3:
        yearlist.append(df_pov.iloc[:,[i]].values.tolist())

    i = i + 1
    
indexer = len(yearlist)
chinapov = (df_pov.loc[df_pov.iloc[:,0] == 'China'] )
chinapov = df_pov.iloc[:,4:44]
chinapoverty = []
chinapoverty = chinapov.values.tolist()



# Create a trace
tracepov = go.Scatter(
    x = yearlist,
    y = chinapoverty
)

data2 = [tracepov]
    


sliderlength = len(df_pov.columns) -1
lijstjes = []


##CHOROPLETH MAP CODE END
traces1 = []
py.sign_in('manolovromero', 'BKTMiBH7jsRXoeDQ1Pvs')
trace1 = {
  "x": ["1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"], 
  "y": [89.52054, 75.80584, 70.90941, 74.31364, 85.49856, 98.48678, 104.3246, 96.58953, 91.47272, 100.1299, 113.163, 118.6546, 131.8836, 157.0904, 160.1401, 178.3418, 165.4055, 185.4228, 156.3964, 183.9832, 194.8047, 197.0715, 203.3349, 225.4319, 250.714, 294.4588, 281.9281, 251.812, 283.5377, 310.8819, 317.8847, 333.1421, 366.4607, 377.3898, 473.4923, 609.6567, 709.4138, 781.7442, 828.5805, 873.2871, 959.3725, 1053.108, 1148.508, 1288.643, 1508.668, 1753.418, 2099.229, 2695.366, 3471.248, 3838.434, 4560.513, 5633.796, 6337.883, 7077.771, 7683.503, 8069.213, 8117.267, 8826.994], 
  "marker": {
    "color": "rgb(8, 247, 0)", 
    "line": {
      "color": "rgb(48, 0, 0)", 
      "width": 1
    }, 
    "opacity": 1
  }, 
  "name": "GDP", 
  "opacity": 1, 
  "type": "bar", 
  "uid": "4cd631", 
  "visible": True, 
  "xsrc": "manolovromero:16:94ff22", 
  "ysrc": "manolovromero:16:ccd68e"
}
traces1.append(trace1)
trace2 = {
  "x": ["1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"], 
  "y": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "24.1", "", "", "20.3", "", "", "12.9", "", "", "13.1", "", "", "10.1", "", "", "4.8", "", "", "3.9", "", "2.7", "1.8", "1.4", "0.4", "0.3", "0.2"], 
  "connectgaps": True, 
  "error_x": {
    "color": "rgb(0, 0, 0)", 
    "symmetric": False, 
    "thickness": 2, 
    "type": "percent", 
    "value": 10, 
    "valueminus": 10, 
    "visible": False, 
    "width": 4
  }, 
  "fill": "none", 
  "line": {
    "color": "rgb(0, 0, 0)", 
    "shape": "spline", 
    "width": 4
  }, 
  "mode": "lines", 
  "name": "Poverty", 
  "opacity": 0.74, 
  "type": "scatter", 
  "visible": True, 
  "xaxis": "x", 
  "xsrc": "manolovromero:16:94ff22", 
  "yaxis": "y2", 
  "ysrc": "manolovromero:16:74919b"
}
traces1.append(trace2)
data = traces1
layouts = {
  "autosize": True, 
  "bargap": 0.24, 
  "bargroupgap": 0, 
  "legend": {"xanchor": "left"}, 
  "title" : "China GDP & Poverty levels"
  , 
  "xaxis": {
    "autorange": False, 
    "domain": [0, 1], 
    "range": [1985, 2017.5], 
    "rangeslider": {
      "autorange": True, 
      "range": [1959.5, 2017.5], 
      "visible": False
    }, 
    "showline": False, 
    "side": "top", 
    "title": {
      "font": {
        "size": 14, 
        "color": "rgb(0, 0, 0)", 
        "family": "Droid Serif"
      }, 
      "text": "Years"
    }, 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "domain": [0, 1], 
    "dtick": 0, 
    "gridcolor": "rgb(204, 21, 21)", 
    "gridwidth": 1, 
    "range": [0, 9291.572631578949], 
    "showgrid": False, 
    "showline": False, 
    "side": "right", 
    "tick0": 0, 
    "tickmode": "auto", 
    "title": {
      "font": {
        "size": 19, 
        "color": "rgb(0, 255, 0)"
      }, 
      "text": "<b>GDP inMillions $</b>"
    }, 
    "type": "linear", 
    "zerolinecolor": "rgb(224, 0, 0)"
  }, 
  "yaxis2": {
    "autorange": False, 
    "fixedrange": False, 
    "gridcolor": "rgb(168, 141, 141)", 
    "overlaying": "y", 
    "range": [0, 25], 
    "showgrid": True, 
    "showline": False, 
    "side": "left", 
    "tickfont": {"color": "rgb(148, 103, 189)"}, 
    "title": {
      "font": {
        "size": 18, 
        "color": "rgb(0, 0, 0)", 
        "family": "Roboto"
      }, 
      "text": "% people sub $1.90"
    }, 
    "type": "linear", 
    "zeroline": True, 
    "zerolinewidth": 0
  }
}

##START Bar chart china


dataaa = [go.Bar(
            x=[
        '1960',
        '1961',
        '1962',
        '1963',
        '1964',
        '1965',
        '1966',
        '1967',
        '1968',
        '1969',
        '1970',
        '1971',
        '1972',
        '1973',
        '1974',
        '1975',
        '1976',
        '1977',
        '1978',
        '1979',
        '1980',
        '1981',
        '1982',
        '1983',
        '1984',
        '1985',
        '1986',
        '1987',
        '1988',
        '1989',
        '1990',
        '1991',
        '1992',
        '1993',
        '1994',
        '1995',
        '1996',
        '1997',
        '1998',
        '1999',
        '2000',
        '2001',
        '2002',
        '2003',
        '2004',
        '2005',
        '2006',
        '2007',
        '2008',
        '2009',
        '2010',
        '2011',
        '2012',
        '2013',
        '2014',
        '2015',
        '2016',
        '2017'
      ],
            y=[
        89.52054,
        75.80584,
        70.90941,
        74.31364,
        85.49856,
        98.48678,
        104.3246,
        96.58953,
        91.47272,
        100.1299,
        113.163,
        118.6546,
        131.8836,
        157.0904,
        160.1401,
        178.3418,
        165.4055,
        185.4228,
        156.3964,
        183.9832,
        194.8047,
        197.0715,
        203.3349,
        225.4319,
        250.714,
        294.4588,
        281.9281,
        251.812,
        283.5377,
        310.8819,
        317.8847,
        333.1421,
        366.4607,
        377.3898,
        473.4923,
        609.6567,
        709.4138,
        781.7442,
        828.5805,
        873.2871,
        959.3725,
        1053.108,
        1148.508,
        1288.643,
        1508.668,
        1753.418,
        2099.229,
        2695.366,
        3471.248,
        3838.434,
        4560.513,
        5633.796,
        6337.883,
        7077.771,
        7683.503,
        8069.213,
        8117.267,
        8826.994
      ]
    )]
    
layout2 = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='yaxis title'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)


##START Bar chart china
##END Bar chart china

##LINE CHART CODE START
title = 'People living in poverty levels (World) x million'


labels = ['3.20$   ', '5.20$   ', '1.90$   ']

colors1 = ['#FF0000','#0083FF' , '#0CFF00']
colors = '#111111'

mode_size = [8, 8, 12]

line_size = [3, 4, 3]




x_data = [
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015, 2020, 2023, 2026, 2029, 2032, 2035, 2039, 2042, 2045],
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015, 2020, 2023, 2026, 2029, 2032, 2035, 2039, 2042, 2045],
    [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015, 2020, 2023, 2026, 2029, 2032, 2035, 2039, 2042, 2045]
]

y_data = [
    [2572, 2709, 2774, 3026, 2999, 3057, 2960, 2751, 2594, 2442, 2299, 2222, 2070, 1929,2006.148156325915, 1909.0715389710822, 1763.4566129388404, 1617.8416869066132, 1472.2267608743714, 1326.6118348421296, 1180.9969088099024, 986.8436741002515, 841.2287480680097, 695.6138220357825],
    [2990, 3183, 3341, 3776, 3908, 4039, 4024, 3939, 3828, 3738, 3663, 3603, 3498, 3384,3580.863987635239, 3547.163833075734, 3496.613601236473, 3446.0633693972195, 3395.5131375579585, 3344.962905718705, 3294.412673879444, 3227.012364760434, 3176.462132921173, 3125.9119010819195],
    [1903, 1868, 1773, 1884, 1706, 1729, 1600, 1350, 1229, 1091, 962, 907, 802, 731,628.0178847427742, 521.4557297416613, 361.6124972400139, 201.76926473835192, 41.926032236704486, 0, 0, 0, 0, 0]

]
# =============================================================================
# 
# xda = [
#     [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015],
#     [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015],
#     [1981, 1984, 1987, 1993, 1996, 1999, 2002, 2005, 2008, 2010, 2011, 2012, 2013, 2015]
# ]
# 
# 
# 
# yda = [
#     [2572, 2709, 2774, 3026, 2999, 3057, 2960, 2751, 2594, 2442, 2299, 2222, 2070, 1929],
#     [2990, 3183, 3341, 3776, 3908, 4039, 4024, 3939, 3828, 3738, 3663, 3603, 3498, 3384],
#     [1903, 1868, 1773, 1884, 1706, 1729, 1600, 1350, 1229, 1091, 962, 907, 802, 731]]
# 
# ##PREDICTION
# regr = LinearRegression()
# 
# 
# 
# for i in range(len(x_data)):
#     xd = np.array(xda[i]).reshape(-1,1)
#     yd = np.array(yda[i])
#     model = LinearRegression()
#     model.fit(xd, yd)
#     predictyears= [2020,2025,2030,2040,2050]
#     X_predict = np.array(predictyears).reshape(-1,1)
#     y_predict = model.predict(X_predict)
#     for j in range(len(y_predict)):
#         y_data.append(str(y_predict[j][0]))
#         x_data.append(str(X_predict[j]))
#     
#         
#     
# =============================================================================





##END PREDICTION

i=0
# =============================================================================
# for row in y_data[0]:
#     y_data[3].append(str(int(y_data[0][i]) + int(y_data[1][i]) + int(y_data[2][i])))
#     i = i + 1
# =============================================================================
    
#print(y_data[3])

names = ['below 3.20$', 'Below 5.20$(total)', 'Below 1.90$']

traces = []

for i in range(0, 3):
    print("hello")
    traces.append(go.Scatter(
        x=x_data[i],
        y=y_data[i],
        name = labels[i],
        mode='lines',
        line=dict(color=colors1[i], width=line_size[i]),
        connectgaps=True,
    ))

    traces.append(go.Scatter(
        x=[x_data[i][0], x_data[i][13]],
        y=[y_data[i][0], y_data[i][13]],
        mode='markers',
        showlegend=False,
        marker=dict(color=colors1[i], size=mode_size[i])
    ))

layout = go.Layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='#FFFFFF',
        linewidth=2,
        ticks='outside',
        tickcolor='#FFFFFF',
        tickwidth=2,
        ticklen=5,
        tickfont=dict(
            family='Arial',
            size=12,
            color='#FFFFFF',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=True,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=True,
    ),
    showlegend=True,
    plot_bgcolor=colors,
    paper_bgcolor=colors,
        legend=dict(
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2
    )
    
)

annotations = []

# Adding labels
for y_trace, label, color in zip(y_data, labels, colors1):
    # labeling the left_side of the plot
    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                  xanchor='right', yanchor='middle',
                                  text=' {}'.format(y_trace[0]),
                                  font=dict(family='Arial',
                                            color='#FFFFFF',
                                            size=12),
                                  showarrow=False))
    # labeling the right_side of the plot
    annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                  xanchor='left', yanchor='middle',
                                  text='{}'.format(y_trace[11]),
                                  font=dict(family='Arial',
                                            color='#FFFFFF',
                                            size=12),
                                  showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text=title,
                              font=dict(family='Arial',
                                        size=24,
                                        color='#FFFFFF'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Kaggle' ,
                              font=dict(family='Arial',
                                        size=12,
                                        color='#FFFFFF'),
                              showarrow=False))

layout['annotations'] = annotations



##LINE CHART CODE END

app.layout = html.Div( children=[
    dcc.Markdown(id="Intro",children=['''
# **Poverty**
##### Welcome to my interactive data story about the UN Development goal of : _Poverty_.
    The goal: end poverty in all its forms everywhere.
    While the world is making some good advancements on reducing poverty, fact is that still a lot of people live below $1.90 a day. 
    This is the most extreme category in poverty data, currently _783_ _MILLION_ people live below this threshold. 
    The goal we are trying to achieve, is divided in several subgoals. They do not only focus on money, but also on:  
    * Stability in the region   
    * Health   
    * Social security    
    * Equality (for every **100** men **122** women live below the poverty threshold).
    So there are quite a few subgoals, but for now I will focus on the money goal.
    The official definition is: 
    **By 2030, eradicate extreme poverty for all people everywhere, currently measured as people living on less than $1.25 a day**
    
    To support the findings and make some sense out of them, I will also provide some   insights about GDP and see how these two factors interact.
    Because there is no dataset for people living below $1.25 a day, I will use one based on $1.90.
 '''])
    ,
    dcc.Markdown(id="Worldtext",children=['''
 \n ### The world
     This is an interactive world map, displaying the percentage of people living below $1.90 a day per country in a given range of years.
     There is a slider attached to the bottom, which you can use the switch between year ranges. 
     If you play around with the slider a little bit, you can see that a lot of countries made / are making really good progress  
     in steering towards the Development goal.
 '''])
    ,
    html.Div(id='newgraph', children=(
        dcc.Graph(
        id='my-graph-id',
        figure={'data': [],
                'layout': {}            
        }
    )   
    ),style={'display': 'inline-block'})
    ,
    html.Div(id='sliderdiv', children=(
    daq.Slider(
        id='my-daq-slider',
        min=4,
        max=sliderlength,
        step=1,
        value=sliderlength-1
    )),style={'width': '96%','padding-left':'35%', 'padding-right':'1%'})
    ,
    
            dcc.Markdown(id="Chinatext",children=['''
## **China**
#### As could be observed above, China went from 25% in the 80's to not even 1% now, that's why I decided to zoom in on China and see what's changed
''']),   
    dcc.Markdown('''
# The History of China's GDP
    This graph compares the changes in GDP and the changes in the amount of people in china living below 1.90$ a day.
    You can see a strong correlation here. China historically didn't have a high GDP and their poverty rate was also quite high. 
    However, when poverty levels reached a record low, GDP started to spike. 
    This trend continued until now, where poverty levels and GDP are reaching western levels. 
    The expected Chinese GDP in 2040 (based on linear regression) is $14.146.000.000.000. 
    However ofcourse, this is just a prediction and the fluctuation is very dependent on many events in the world.
'''),
 html.Div(id='Chinagdp', style={'textAlign': 'center'},
                                       children=[
                

dcc.Graph(
        id='Chinachart',
        
        figure={'data':traces1  , 'layout': layouts        
        }
    ),    
     dcc.Markdown('''

    
''')
    
            ])

,      

       







                      
    html.Div(id='4linespovgraph', style={'textAlign': 'center', 'display': 'inline-block'},
                                       children=[
                dcc.Markdown('''
# The course of poverty levels over the years

    The most extreme form of poverty(sub $1.90) is making really promising progress.  
    It is predicted (Regression) that in 2035 this form is completely eradicated,
    and that the second threshold(sub $3.20) will become half of what it used to be.
    The $5.20 threshold in contrast to the others, is making less progress. 
    In my opinion this is due to the fact that the people escaping from the lower two levels are first and still passing
    through the third level. 
    Also: With inflation in mind, the goal should be adjusted. The worth of $1.90 now is probably slightly higher in the future.
    
    
                
                             
''')
,
dcc.Graph(
        id='Line chart',
        
        figure={'data': traces,
                'layout': layout            
        }
    )
            ]),                                              

    

    
],        style={
        'padding-left':'20%','width': 1000,'textAlign': 'center','padding-right':'1%'
    })
    
@app.callback(
    dash.dependencies.Output('newgraph', 'children'),
    [dash.dependencies.Input('my-daq-slider', 'value')])

def update_output_graph(input_value):
    if input_value < 4:
        input_value = 4
    return dcc.Graph(
        id='my-graph-id',

        figure={'data': [go.Choropleth(
    locations = df_pov['Country Code'],
    z = df_pov.iloc[:,int(input_value)],
    text = df_pov['Country Name'],
    
    autocolorscale = True,
    reversescale = False,
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(180,180,180)',
            width = 0.5
        )),
    colorbar = go.choropleth.ColorBar(
        tickprefix = '%',
        title = '%  below 1.90$ '),
)],
                'layout': go.Layout(
    title = go.layout.Title(
        text = list(df_pov)[int(input_value)]
    ),
    geo = go.layout.Geo(
        showframe = False,
        showcoastlines = False,
        projection = go.layout.geo.Projection(
            type = 'equirectangular'
        )
    ),
    annotations = [go.layout.Annotation(
        x = 0.55,
        y = 0.1,
        xref = 'paper',
        yref = 'paper',
        text = 'Source: Kaggle',
        showarrow = False
    )]
)            
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)


input("hoi")
