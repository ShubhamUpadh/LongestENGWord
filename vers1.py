# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:46:10 2022

@author: 91995
"""
import dash
import dash_bootstrap_components as dbc
import html as html
from dash import html
import datetime

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
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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

        dbc.Row([html.Div(html.B("I will tell you the longest english word that doesn't contain the entered alphabets."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 20})
                 ]),

        dbc.Row([html.Div(html.B("For example, the longest word that doesn't contain the alphabets (a, x, i,"
                                 " s) is HYDROMETEOROLOGY."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 40, 'marginTop': 30})
                 ]),



    ])

])
if __name__ == "__main__":
    app.run_server(debug=True)
