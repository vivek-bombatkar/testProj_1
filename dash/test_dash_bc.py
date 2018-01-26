
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output, Event

app = dash.Dash()

app.config['suppress_callback_exceptions']=True

app.layout = html.Div(children=[
    html.H1(children='Blockchain usecase'),

    html.Label('Input Data Set  '),
    dcc.Input(id='input',value='',type='text'),

    html.Label('Result Data Set '),
    html.Div(id='output'),

    html.Button(id='Button_1',  children='Process Data set', n_clicks=0),
    html.Div(id=' '),

    html.Label('add to bc '),
    html.Div(id='output_bc')
])

@app.callback(
    Output('output_bc', 'children'),
    [Input('Button_1', 'n_clicks')])
def update_output(n_clicks):
    return ' # : ' + str(n_clicks)


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(n_clicks):
    return ' # : ' + str(n_clicks)[::-1]


if __name__ == '__main__':
    app.run_server(debug=True)