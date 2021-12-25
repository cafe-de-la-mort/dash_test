# Third-party Imports
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px

# Initializations
app = dash.Dash()   #initialising dash app
df = px.data.stocks() #reading stock price dataset


def goog_stock_prices():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x = df['date'], y = df['GOOG'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig


def aapl_stock_prices():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x = df['date'], y = df['AAPL'],\
                     line = dict(color = 'blue', width = 4), name = 'Apple')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),


        dcc.Graph(id = 'goog_line_plot', figure = goog_stock_prices()),

        dcc.Graph(id = 'aapl_line_plot', figure = aapl_stock_prices())
    ]
                     )

if __name__ == '__main__':
    app.run_server()
