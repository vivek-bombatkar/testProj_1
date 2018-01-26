
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
    dcc.Input(value='', type='text'),
#type='submit',
    html.Button(id='Button_1',  children='Process Data set', n_clicks=0),
    html.Div(id='output')
])

@app.callback(
    Output('update_output', 'children'),
    [Input('Button_1', 'n_clicks')],
    [State('Button_1', 'n_clicks')])
def update_output(b1_clicks, prev_b1_clicks):
    if b1_clicks > prev_b1_clicks:
        return 'Button 1 Was Clicked'.format(prev_b1_clicks, b1_clicks)

#for state_id, evend_id in id_pairs:
#    @app.callback(Output('target', 'children'), [], [State(state_id, 'value')], [Event(event_id, 'click'))(your_callback_function)\
#@app.callback(Output('target', 'children'), [], [State('input', 'value')], [Event('submit', 'click')])
#def callback(state):
#    return "callback received value: {}".format(state)



if __name__ == '__main__':
    app.run_server(debug=True)