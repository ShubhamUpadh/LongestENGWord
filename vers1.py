# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:46:10 2022

@author: 91995
"""
import dash
import csv
import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc

colors = {
    'background': '#000000'
}

borderInf = {
    'Inf': '5px solid gray',
    'Inf1': '1px #898989'
}

textCol = {
    'text': '#FFF'
}

# grad ={
# 'gr': 'linearGradient('red','yellow')'
# }
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = "Wordominator"

app.layout = html.Div(style={'paddingTop': 50}, children=[

    dbc.Container([

        dbc.Row([
            html.Div(html.B("WORDOMINATOR"), style={'fontSize': 40, 'color': '#FFF', 'textAlign': 'center',
                                                    'marginBottom': 40})

        ]),

        dbc.Row([
            html.Div(html.B("Hello and Welcome !"), style={'fontSize': 25, 'color': '#FFF', 'textAlign': 'center',
                                                           'marginBottom': 10})

        ]),

        dbc.Row([html.Div(html.B("I will tell you the longest english dictionary word that doesn't contain the "
                                 "entered alphabets."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 20})
                 ]),

        dbc.Row([html.Div(html.B("For example, the longest dictionary word that doesn't contain the alphabets (a, x, i,"
                                 " s) is HYDROMETEOROLOGY."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 30, 'marginTop': 30})
                 ]),

        html.Hr(style={'color': '#FFF'}),

        dbc.Row([html.Div(html.B("Enter the alphabets that the word SHOULD NOT contain : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 5, 'marginTop': 15})
                 ]),

        dbc.Row(
            [html.Div(dcc.Input(id='my-input', value='', type='text'),
                      style={'marginTop': 0, 'textAlign': 'center', 'fontSize': 20, 'color': '#FFF'})
             ]),

        html.Br(),

        dbc.Row([html.Div(html.B(id='my-output'),
                          style={'marginTop': 10, 'marginBottom': 15, 'textAlign': 'center', 'fontSize': 20,
                                 'color': '#FFF'})
                 ]),

        html.Hr(style={'color': '#FFF'})

    ])

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    check = True

    if len(input_value) == 0:
        return "NO INPUT DETECTED"
    z = list()
    for alpha in input_value:
        if alpha.isalpha() and not alpha in z:
            z.append(alpha)
            check = False

    if check:
        return "NO INPUT DETECTED"

    print(z)

    lenWord = 0
    longestWord = ""

    with open("dictionaryedited1.csv", mode='r') as file:
        fileF = csv.reader(file)
        for lines in fileF:

            flag = True

            for alphabet in z:
                if alphabet.lower() in str(lines) or alphabet.upper() in str(lines):
                    flag = False
                    break

            if flag and lenWord < len(str(lines)) and not " " in str(lines):
                longestWord = str(lines)
                lenWord = len(str(lines))

    if longestWord == "" or len(longestWord) == 5:
        return "No such word exists :( "

    elif input_value in ('Bijoy', 'bijoy'):
        return "BIJOY JADAV"

    elif input_value == 'Vivek':
        return "MANAGER MARAJ"

    else:
        return str(longestWord[2:-2]).upper()


if __name__ == "__main__":
    app.run_server(debug=True)
