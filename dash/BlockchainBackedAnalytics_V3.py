
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output, Event
import time
from textblob import TextBlob
import dash_table_experiments as dt
import pandas as pd
import io
import base64
import dash_table_experiments as dt


#impliment the blockhain
import datetime as date
import hashlib as hash

global prev_block
input_data_set = ''
data_science_module = ''
result_data_set = ''

class Block:
    def __init__(self, index, timestamp, data, indexOfParent, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.indexOfParent = indexOfParent
        self.prev_hash = prev_hash
        self.hash = hash.sha256(data.encode('ascii')).hexdigest()

    def __repr__(self):
        return "{0} : {1}, {2}, {3} ".format(self.index, str(self.timestamp), self.data, self.indexOfParent, self.prev_hash)

def getGenesisBlock():
    return Block(0, date.datetime.now(), "the genesis block", 0, "0")

def getNextBlock(prev_block, data, indexOfParent ):
    index = prev_block.index + 1
    timestamp = date.datetime.now()
    data = data
    indexOfParent = indexOfParent
    hash = prev_block.hash
    return Block(index, timestamp, data, indexOfParent, hash)

#the datascience module
def getSentimentsPolarity(inputData):
    return str(TextBlob(inputData).sentiment.polarity)

def addToBlockchain(prev_block,inputData,value_data_science_module,result_data_set):
    #result = getSentimentsPolarity(inputData)
    time.sleep(1)
    #add input to bc
    new_block = getNextBlock(prev_block, hash.sha256(inputData.encode('ascii')).hexdigest(), 0)
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add code to bc
    new_block = getNextBlock(prev_block, hash.sha256(value_data_science_module.encode('ascii')).hexdigest(), prev_block.index)
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add result to bc
    new_block = getNextBlock(prev_block, hash.sha256(result_data_set.encode('ascii')).hexdigest(), prev_block.index)
    bc.append(new_block)
    return ""

##### THE DASH PAGE
app = dash.Dash()
app.scripts.config.serve_locally = True

app.config['suppress_callback_exceptions']=True

all_options = {
    'Data': [''],
    'Module': [''],
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
                html.H1('Data'),
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
            ]
        ),

        # Tab 2
        html.Div(
            id='ModelBlock',
            style={'display': 'none'},
            children=[
                html.H1('Model'),
                dcc.Upload(
                    id='upload_data_science_module',
                    children=html.Div([
                        'Data_Science_Module - Drag and Drop or ',
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
                html.Div([
                    dcc.Textarea(id='train_data_tx_id', placeholder='Enter Blockchain Transaction ID for Train data...', rows=1, style={'width': '50%','margin': '10px'})
                ]),
            ]
        ),

        # Tab 3
        html.Div(
            id='ResultBlock',
            style={'display': 'none'},
            children=[
                html.H1('Result'),
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
                html.Div([
                    dcc.Textarea(id='model_tx_id', placeholder='Enter Blockchain Transaction ID for Model...', rows=1, style={'width': '50%','margin': '10px'})
                ]),
                html.Div([
                    dcc.Textarea(id='input_data_tx_id', placeholder='Enter Blockchain Transaction ID for Input data...',
                                 rows=1, style={'width': '50%','margin': '10px'})
                ]),
            ]
        ),
    ]),
    html.H6(children='HASH of the uploaded data...'),
    html.Div(id='file_hash'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),

    html.Button(id='Button_1',  children='Add to blockchain', n_clicks=0),
    html.Div(id=' '),

    html.Label(' '),
    html.Div(id='output_bc'),

    html.Pre(id='output', className='six columns')
])


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

#show file hash
@app.callback(Output('file_hash', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_module(filename,contents):
    global result_data_set
    hash_contents = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([
        html.H6(hash_contents),
        html.Hr(),  # horizontal lines
    ])

#show blockchain
@app.callback(
    Output('output_bc', 'children'),
    [Input('Button_1', 'n_clicks')])
def update_output(n_clicks):
    if n_clicks == 0:
        return ''
    prev_block = bc[len(bc)-1]
    addToBlockchain(prev_block,str(input_data_set),str(data_science_module),str(result_data_set))
#            value="Input at blockchain index : {1}, Code at blockchain index : {2}, Result at blockchain index : {3} ,".format(str(bc[len(bc)-3].index()),str(bc[len(bc)-2].index()),str(bc[len(bc)-1].index())) ,
    return html.Div([
        html.Div([dcc.Textarea(
            #value=" # " + str(value_input_data_set) + " : " + str(value_data_science_module),
            value="blockchain index {} : Input Data Set \nblockchain index {} : Data science module / Code \nblockchain index {} : Result".format(str(bc[len(bc)-3].index),str(bc[len(bc)-2].index),str(bc[len(bc)-1].index)) ,
                               id='dynamic-output',style={'width': '100%'})]),
        html.Div([html.H6("Index : Timestamp, HASH of the data, Parent block", style={'width': '100%'})]),
        html.Div([
            dcc.Input(
                value='{} : {} , {} , {}'.format(block.index,block.timestamp,block.hash,block.indexOfParent),
                id='input-{}'.format(block.index),
                style={'width': '100%'}
            )
            for block in bc
        ]),
        html.Div(id='dynamic-output')
    ])

#show file
@app.callback(Output('input_data_set', 'children'),
              [Input('upload_input_data_set', 'filename') , Input('upload_input_data_set', 'contents')])
def upload_input_data_set(filename, contents):
    global input_data_set
    input_data_set = contents
    return html.Div([
        html.H6(filename),
        html.Hr(),  # horizontal lines
    ])

#show file
@app.callback(Output('data_science_module', 'children'),
              [Input('upload_data_science_module', 'filename'),Input('upload_data_science_module', 'contents')])
def upload_data_science_module(filename,contents):
    global data_science_module
    data_science_module = contents
    return html.Div([
        html.H6(filename),
        html.Hr(),  # horizontal lines
    ])

#show file
@app.callback(Output('result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_module(filename,contents):
    global result_data_set
    result_data_set = contents
    return html.Div([
        html.H6(filename),
        html.Hr(),  # horizontal lines
    ])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    #add the very first block to the blockchain
    button_n_clicks = 0
    bc = [getGenesisBlock()]
    prev_block = bc[0]
    app.run_server(debug=True)