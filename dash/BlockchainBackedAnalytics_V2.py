
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
global button_n_clicks

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
    return str(TextBlob(inputData).sentiment.polarity)

def addToBlockchain(prev_block,inputData,value_data_science_module,result_data_set):
    #result = getSentimentsPolarity(inputData)
    time.sleep(1)
    #add input to bc
    new_block = getNextBlock(prev_block, hash.sha256(inputData.encode('ascii')).hexdigest())
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add code to bc
    new_block = getNextBlock(prev_block, hash.sha256(value_data_science_module.encode('ascii')).hexdigest())
    bc.append(new_block)
    prev_block = new_block
    time.sleep(1)
    #add result to bc
    new_block = getNextBlock(prev_block, hash.sha256(result_data_set.encode('ascii')).hexdigest())
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
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '20%',
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
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '20%',
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
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '20%',
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
###
#    html.Label('Input Data Set  '),
#    dcc.Textarea(id='input',value='', style={'width': '100%'}),

#    html.Label('Result '),
#    html.Div(id='output'),

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
    [Input('Button_1', 'n_clicks'),
    Input('upload_input_data_set', 'contents'),
    Input('upload_data_science_module', 'contents'),
    Input('upload_result_data_set', 'contents')])
def update_output(n_clicks,value_input_data_set,value_data_science_module,result_data_set):
    if n_clicks == 0:
        return ''
    button_n_clicks = n_clicks
    prev_block = bc[len(bc)-1]
    print(str(value_input_data_set))
    print(str(value_data_science_module))
    print(str(result_data_set))
    addToBlockchain(prev_block,str(value_input_data_set),str(value_data_science_module),str(result_data_set))
#            value="Input at blockchain index : {1}, Code at blockchain index : {2}, Result at blockchain index : {3} ,".format(str(bc[len(bc)-3].index()),str(bc[len(bc)-2].index()),str(bc[len(bc)-1].index())) ,
    return html.Div([
        html.Div([dcc.Textarea(
            #value=" # " + str(value_input_data_set) + " : " + str(value_data_science_module),
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

#show file
@app.callback(Output('input_data_set', 'children'),
              [Input('upload_input_data_set', 'filename')])
def upload_input_data_set(filename):
    return html.Div([
        html.H5(filename),
        html.Hr(),  # horizontal lines
    ])

#show file
@app.callback(Output('data_science_module', 'children'),
              [Input('upload_data_science_module', 'filename')])
def upload_data_science_module(filename):
    return html.Div([
        html.H5(filename),
        html.Hr(),  # horizontal lines
    ])

#show file
@app.callback(Output('result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename')])
def upload_data_science_module(filename):
    return html.Div([
        html.H5(filename),
        html.Hr(),  # horizontal lines
    ])

def update_output(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        if 'csv' in content_type:
            df = pd.read_csv(io.StringIO(base64.b64decode(content_string).decode('utf-8')))
            return html.Div([
                dt.DataTable(rows=df.to_dict('records')),
                html.Hr(),
                html.Div('Raw Content'),
                html.Pre(contents, style=pre_style)
            ])
        elif 'image' in content_type:
            return html.Div([
                html.Img(src=contents),
                html.Hr(),
                html.Div('Raw Content'),
                html.Pre(contents, style=pre_style)
            ])
        else:
            # xlsx will have 'spreadsheet' in `content_type` but `xls` won't
            # have anything
            try:
                df = pd.read_excel(io.BytesIO(base64.b64decode(content_string)))
                return html.Div([
                    dt.DataTable(rows=df.to_dict('records')),
                    html.Hr(),
                    html.Div('Raw Content'),
                    html.Pre(contents, style=pre_style)
                ])
            except:
                return html.Div([
                    html.Hr(),
                    html.Div('ONLY Raw Content : ' + content_type + " : " + content_string),
                    html.Pre(contents, style=pre_style)
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