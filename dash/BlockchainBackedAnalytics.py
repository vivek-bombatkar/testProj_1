
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output, Event
import blockChain as blockChain

inputFileHash=''
dataScienceModelHash=''
resultDataHash=''

input_data_set = ''
data_science_model = ''
result_data_set = ''

n_clicks_data_set_cnt=0
n_clicks_model_cnt=0
##### THE DASH PAGE START
app = dash.Dash()
app.scripts.config.serve_locally = True

app.config['suppress_callback_exceptions']=True

all_options = {
    'Data': [''],
    'model': [''],
    'Result': ['']
}


pre_style = {
    'whiteSpace': 'pre-wrap',
    'wordBreak': 'break-all',
    'whiteSpace': 'normal'
}
tab_style = {
    'color': '#0074D9',
    'text-decoration': 'underline',
    'margin': 30,
    'cursor': 'pointer'
}
app.layout = html.Div(children=[
    html.H1(children='Blockchain Backed Analytics'),
    html.Hr(),
    dcc.Location(id='url'),
    dcc.Link('Data', href='/DataBlock', style=tab_style),
    dcc.Link('Model', href='/ModelBlock', style=tab_style),
    dcc.Link('Result', href='/ResultBlock', style=tab_style),
    html.Div([

        # Tab 1
        html.Div(
            id='DataBlock',
            style={'display': 'none'},
            children=[
                html.H3('Data'),
                dcc.Upload(
                    id='upload_input_data_set',
                    children=html.Div([
                        'Input Data Set - Drag and Drop or ',
                        html.A('Select a File')
                    ]),
                    style={
                        'width': '50%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    }
                ),
                html.Div(id='input_data_set'),
                html.Div(id='file_hash_data_set'),
                html.Button(id='button_data_set', children='Add to blockchain input', n_clicks=0),
                html.Div(id=' '),
            ]
        ),

        # Tab 2
        html.Div(
            id='ModelBlock',
            style={'display': 'none'},
            children=[
                html.H3('Model'),
                dcc.Upload(
                    id='upload_data_science_model',
                    children=html.Div([
                        'Data_Science_model - Drag and Drop or ',
                        html.A('Select a File')
                    ]),
                    style={
                        'width': '50%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    }
                ),
                html.Div([dcc.Textarea(id='train_data_tx_id', placeholder='Enter Blockchain Transaction ID for Train data...',value='', rows=1, style={'width': '50%','margin': '10px'}) ]),
                html.Div(id='data_science_model'),
                html.Div(id='file_hash_model'),
                html.Button(id='Button_model', children='Add to blockchain', n_clicks=0),
                html.Div(id=' '),
            ]
        ),

        # Tab 3
        html.Div(
            id='ResultBlock',
            style={'display': 'none'},
            children=[
                html.H3('Result'),
                dcc.Upload(
                    id='upload_result_data_set',
                    children=html.Div([
                        'Result Data Set - Drag and Drop or ',
                        html.A('Select a File')
                    ]),
                    style={
                        'width': '50%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    }
                ),
                html.Div([dcc.Textarea(id='model_tx_id', placeholder='Enter Blockchain Transaction ID for Model...', rows=1, style={'width': '50%','margin': '10px'})]),
                html.Div([dcc.Textarea(id='input_data_tx_id', placeholder='Enter Blockchain Transaction ID for Input data...',rows=1, style={'width': '50%','margin': '10px'})]),
                html.Div(id='result_data_set'),
                html.Div(id='file_hash_result_data_set'),
                html.Button(id='Button_result_data_set', children='Add to blockchain', n_clicks=0),
                html.Div(id=' '),
            ]
        ),
    ]),
    html.Label(' '),
    html.Div(id='output_bc'),

    html.Pre(id='output', className='six columns')
])
##### THE DASH PAGE ENDS
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

def generate_display_tab(tab):
    def display_tab(pathname):
        if tab == 'DataBlock' and (pathname is None or pathname == '/'):
            return {'display': 'block'}
        elif pathname == '/{}'.format(tab):
            return {'display': 'block'}
        else:
            return {'display': 'none'}
    return display_tab


for tab in ['DataBlock', 'ModelBlock', 'ResultBlock']:
    app.callback(Output(tab, 'style'), [Input('url', 'pathname')])(
        generate_display_tab(tab)
    )

#show file hash start#
@app.callback(Output('file_hash_data_set', 'children'),
              [Input('upload_input_data_set', 'filename'),Input('upload_input_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global inputFileHash
    inputFileHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([ html.H6(inputFileHash)])

@app.callback(Output('file_hash_model', 'children'),
              [Input('upload_data_science_model', 'filename'),Input('upload_data_science_model', 'contents')])
def upload_data_science_model(filename,contents):
    global dataScienceModelHash
    dataScienceModelHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([html.H6(dataScienceModelHash)])

@app.callback(Output('file_hash_result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global resultDataHash
    resultDataHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([html.H6(resultDataHash)])
#show file hash start#
#show file name start#
@app.callback(Output('input_data_set', 'children'),
              [Input('upload_input_data_set', 'filename') , Input('upload_input_data_set', 'contents')])
def upload_input_data_set(filename, contents):
    global input_data_set
    input_data_set = contents
    return html.Div([html.H6(filename)])

@app.callback(Output('data_science_model', 'children'),
              [Input('upload_data_science_model', 'filename'),Input('upload_data_science_model', 'contents')])
def upload_data_science_model(filename,contents):
    global data_science_model
    data_science_model = contents
    return html.Div([html.H6(filename)])

@app.callback(Output('result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global result_data_set
    result_data_set = contents
    return html.Div([html.H6(filename)])
#show file name#
#add to blockchain
@app.callback(
    Output('output_bc', 'children'),
    [Input('button_data_set', 'n_clicks'), Input('Button_model', 'n_clicks'), Input('Button_result_data_set', 'n_clicks')],
    [State('train_data_tx_id', 'value'),State('model_tx_id', 'value'),State('input_data_tx_id', 'value')])
def update_output(n_clicks_data_set,n_clicks_model,n_clicks_result_data_set,value_train_data_tx_id,value_model_tx_id,value_input_data_tx_id):
    global n_clicks_data_set_cnt
    global n_clicks_model_cnt

    if n_clicks_data_set == 0 and n_clicks_model == 0 and n_clicks_result_data_set == 0:
        return ''
    prev_block = bc[len(bc)-1]
    if n_clicks_data_set_cnt <> n_clicks_data_set:
        data = "{{ hash_data: {} }}".format(inputFileHash)
    elif n_clicks_model_cnt <> n_clicks_model:
        data = "{{ hash_model: {}, Index_training_data: {} }}".format(dataScienceModelHash,value_train_data_tx_id)
    else:
        data = "{{ hash_result_data: {}, Index_model: {}, Index_input_data: {} }}".format(resultDataHash,value_model_tx_id,value_input_data_tx_id )

    new_block = blockChain.getNextBlock(prev_block, data)
    bc.append(new_block)
    n_clicks_data_set_cnt = n_clicks_data_set
    n_clicks_model_cnt = n_clicks_model
    return html.Div([
#        html.Div([dcc.Textarea(value="Block added to index {} ".format(str(bc[len(bc)-1].index)) ,id='dynamic-output',style={'width': '100%'})]),
#        html.Div([html.H6("Index : Timestamp, Data", style={'width': '100%'})]),
        html.Div([
            dcc.Input(
                value='{} : {} , {} '.format(block.index,block.timestamp,block.data),
                id='input-{}'.format(block.index),
                style={'width': '100%'}
            )
            for block in bc
        ]),
        html.Div(id='dynamic-output')
    ])

if __name__ == '__main__':
    #add the very first block to the blockchain
    button_n_clicks = 0
    bc = [blockChain.getGenesisBlock()]
    app.run_server(debug=True)