from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('winequelity.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div([
    html.Div([
        generate_table(df)
    ]), 
    html.Div([
        dcc.RadioItems(
            ['Regression', 'Classification'],
            'Regression',
            id='xaxis-type',
            inline=True
        ),
        dcc.Dropdown(
            df.columns,
            'density',
            id='xaxis-column'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    dcc.Graph(id='indicator-graphic')
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('xaxis-type', 'value'))

def update_graph(xaxis_column_name, xaxis_type):
    if xaxis_type == 'Regression':
        
        fig = px.scatter(x=df[xaxis_column_name], y=df['pH'])
        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0})
        fig.update_xaxes(title=xaxis_column_name, type='linear')
        fig.update_yaxes(title='pH', type='linear')

        return fig
    
    else:
        
        dff = pd.read_csv('winequelity.csv')        
        dff = dff.groupby(['target', dff[xaxis_column_name]]).sum().reset_index(level=[0,1])        
        fig = px.bar(x=dff['target'], y=dff[xaxis_column_name], color=dff['target'], color_discrete_sequence=["red", "blue"])        
        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0})
        fig.update_xaxes(title='target')
        fig.update_yaxes(title=xaxis_column_name)

        return fig

if __name__ == '__main__':
    app.run_server(debug=True)