import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['DATA', 'MODULE', 'RESULT'  ]],
        value=None,
        disabled=True
    ),
    html.Br(),
    html.Div([
        dcc.Textarea(id='input_query',placeholder='Enter/Review Query...',rows=1,style={'width': '50%'},disabled=True)
    ]),
    html.Br(),
    html.Div([
        dcc.Textarea(id='input_query',placeholder='Enter/Review Query...',rows=1,style={'width': '50%'},disabled=True)
    ]),
    html.Br(),
    html.Button('Add Option', id='button', n_clicks=0)
])



if __name__ == '__main__':
    app.run_server(debug=True)
