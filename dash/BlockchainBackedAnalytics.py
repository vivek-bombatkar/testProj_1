
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output, Event
import time
import pandas as pd
import io
import dash_table_experiments as dt
#from textblob import TextBlob

#impliment the blockhain
import datetime as date
import hashlib as hash

global prev_block

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hash.sha256(data.encode('ascii')).hexdigest()

    def __repr__(self):
        return "{0} : {1}, {2}, {3} ".format(self.index, str(self.timestamp), self.data, self.prev_hash)

def getGenesisBlock():
    return Block(0, date.datetime.now(), "the genesis block", "0")

def getNextBlock(prev_block, data):
    index = prev_block.index + 1
    timestamp = date.datetime.now()
    data = data
    hash = prev_block.hash
    return Block(index, timestamp, data, hash)

#the datascience module
def getSentimentsPolarity(inputData):
    return ""#str(TextBlob(inputData).sentiment.polarity)

def addToBlockchain(prev_block,inputData):
    result = getSentimentsPolarity(inputData)
    time.sleep(1)
    #add input to bc
    new_block = getNextBlock(prev_block, hash.sha256(inputData.encode('ascii')).hexdigest())
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add code to bc
    new_block = getNextBlock(prev_block, hash.sha256("TextBlob(inputData).sentiment.polarity".encode('ascii')).hexdigest())
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add result to bc
    new_block = getNextBlock(prev_block, hash.sha256(result.encode('ascii')).hexdigest())
    bc.append(new_block)
    return ""

app = dash.Dash()

app.config['suppress_callback_exceptions']=True

app.layout = html.Div(children=[
    html.H1(children='Blockchain Backed Analytics'),

    html.Label('Input Data Set  '),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
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
        },
        # Allow multiple files to be uploaded
        #multiple=True
    ),
dt.DataTable(
        id='datatable',
        rows=[{}]
    ),
    dcc.Textarea(id='input',value='', style={'width': '100%'}),

    html.Label('Result '),
    html.Div(id='output'),

    html.Button(id='Button_1',  children='Add to blockchain', n_clicks=0),
    html.Div(id=' '),

    html.Label('add to bc '),
    html.Div(id='output_bc')
])


@app.callback(
    Output('datatable', 'rows'),
    [Input('upload-data', 'contents')])
def update_figure(content):
    if not content:
        return []
    dff = pd.read_csv(io.StringIO(content))
    return dff.to_dict('records')


#show blockchain
@app.callback(
    Output('output_bc', 'children'),
    [Input('Button_1', 'n_clicks')],
    [State('input', 'value')])
def update_output(n_clicks,value):
    if n_clicks == 0:
        return ''
    prev_block = bc[len(bc)-1]
    addToBlockchain(prev_block,value)
#            value="Input at blockchain index : {1}, Code at blockchain index : {2}, Result at blockchain index : {3} ,".format(str(bc[len(bc)-3].index()),str(bc[len(bc)-2].index()),str(bc[len(bc)-1].index())) ,
    return html.Div([
        html.Div([dcc.Textarea(
            value="blockchain index {} : Input Data Set \nblockchain index {} : Data science module / Code \nblockchain index {} : Result".format(str(bc[len(bc)-3].index),str(bc[len(bc)-2].index),str(bc[len(bc)-1].index)) ,
                               id='dynamic-output',style={'width': '100%'})]),
        html.Div([
            dcc.Input(
                value='{}'.format(block),
                id='input-{}'.format(block.index),
                style={'width': '100%'}
            )
            for block in bc
        ]),
        html.Div(id='dynamic-output')
    ])

#show result
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(value):
    return (str(getSentimentsPolarity(str(value))))

if __name__ == '__main__':
    #add the very first block to the blockchain
    bc = [getGenesisBlock()]
    prev_block = bc[0]
    app.run_server(debug=True)