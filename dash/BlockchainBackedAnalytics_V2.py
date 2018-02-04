
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


app.layout = html.Div(children=[
    html.H1(children='Blockchain Backed Analytics'),
###
    html.Div(id='waitfor'),
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
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none', 'min_width': '777', 'min_height' :'555' }),
###
###
    html.Div(id='waitfor'),
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

    html.Div(id='data_science_module'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
###
###
    html.Div(id='waitfor'),
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

    html.Div(id='result_data_set'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),

    html.Button(id='Button_1',  children='Add to blockchain', n_clicks=0),
    html.Div(id=' '),

    html.Label(' '),
    html.Div(id='output_bc')
])
pre_style = {
    'whiteSpace': 'pre-wrap',
    'wordBreak': 'break-all',
    'whiteSpace': 'normal'
}


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