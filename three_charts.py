

import pandas
import plotly
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

#fig.show() - this does not work 
plotly.offline.plot(fig)  #code works !!! -- reference : https://stackoverflow.com/questions/61766508/site-cannot-be-reached-when-graph-using-plotly/62215075#62215075 



#import plotly.express as px
#df = px.data.tips()
#fig = px.bar(df, x="total_bill", y="day", orientation='h')
#fig.show()
#
#
#import plotly.express as px
#df = px.data.tips()
#fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
#             hover_data=["tip", "size"],
#             height=400,
#             title='Restaurant bills')
#fig.show()



#import plotly.graph_objects as go
#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True)
#
#import plotly.graph_objects as go
#fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
#fig







# CHART 1 (PIE)
#

#pie_data = [
#    {"company": "Company X", "market_share": 0.55},
#    {"company": "Company Y", "market_share": 0.30},
#    {"company": "Company Z", "market_share": 0.15}
#]
#
#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data
#
##
## CHART 2 (LINE)
##
#
#line_data = [
#    {"date": "2019-01-01", "stock_price_usd": 100.00},
#    {"date": "2019-01-02", "stock_price_usd": 101.01},
#    {"date": "2019-01-03", "stock_price_usd": 120.20},
#    {"date": "2019-01-04", "stock_price_usd": 107.07},
#    {"date": "2019-01-05", "stock_price_usd": 142.42},
#    {"date": "2019-01-06", "stock_price_usd": 135.35},
#    {"date": "2019-01-07", "stock_price_usd": 160.60},
#    {"date": "2019-01-08", "stock_price_usd": 162.62},
#]
#
#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data
#
##
## CHART 3 (HORIZONTAL BAR)
##
#
#bar_data = [
#    {"genre": "Thriller", "viewers": 123456},
#    {"genre": "Mystery", "viewers": 234567},
#    {"genre": "Sci-Fi", "viewers": 987654},
#    {"genre": "Fantasy", "viewers": 876543},
#    {"genre": "Documentary", "viewers": 283105},
#    {"genre": "Action", "viewers": 544099},
#    {"genre": "Romantic Comedy", "viewers": 121212}
#]
#
#print("----------------")
#print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data