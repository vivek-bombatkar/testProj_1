#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html


def generate_inputs():
    print('getting value!')
    f = open('C:\\VIVEK\\WORKING\\NOTES\\REGRASSION_TESTIN.txt', 'r')
    current_value = str(f.read())
    f.close()

    print('current_value: ' + str(current_value))

    input_box = [html.Label(html.Strong('value to write; currently: ')),
                 dcc.Input(type='number', value=current_value, id='input_value')]

    return input_box


app = dash.Dash()

app.layout = html.Div([
    html.H2('debug: getting and setting'),

    html.Div(
        generate_inputs()
    ),

    html.Div(id='file_value_written')

])  # app.layout


@app.callback(
    dash.dependencies.Output(component_id='file_value_written', component_property='children'),
    [dash.dependencies.Input(component_id='input_value', component_property='value')])
def update_file_value(value_to_write):
    print('set value!')
    print('value_to_write: ' + str(value_to_write))
    f = open('./value.txt', 'w')
    f.write(str(value_to_write))
    f.close()

    return value_to_write


if __name__ == '__main__':
    app.run_server(debug=True)