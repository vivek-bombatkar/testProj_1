import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import base64
import json
import pandas as pd
import plotly
import io

app = dash.Dash()
app.config['suppress_callback_exceptions']=True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(id='waitfor'),
    dcc.Upload(
        id='upload',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
    dt.DataTable(
        id='datatable',
        rows=[{}]
    ),
])

pre_style = {
    'whiteSpace': 'pre-wrap',
    'wordBreak': 'break-all',
    'whiteSpace': 'normal'
}

@app.callback(
    Output('datatable', 'rows'),
    [Input('upload', 'contents')])
def update_figure(content):
    if not content:
        return []
    print(content)
    dff = pd.read_csv(io.StringIO(content))
    return dff.to_dict('records')



app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)