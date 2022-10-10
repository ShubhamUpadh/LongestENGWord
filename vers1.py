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
from dash.dependencies import Input, Output
from dash import dcc

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

ALLOWED_TYPES = (
    "text"
)
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

        dbc.Row(
            [html.Div(html.B("I will tell you the longest english word that doesn't contain the entered alphabets."),
                      style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                             'marginBottom': 20})
             ]),

        dbc.Row([html.Div(html.B("For example, the longest word that doesn't contain the alphabets (a, x, i,"
                                 " s) is HYDROMETEOROLOGY."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 20, 'marginTop': 20})
                 ]),

        html.Hr(style={'color': '#FFF', 'height': 2}),

        dbc.Row([html.Div(html.B("Enter the alphabets that you don't want the target word to contain  "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 40, 'marginTop': 20})
                 ]),

        html.Div(
            [
                dcc.Input(
                    id="input_{}".format(_),
                    type=_,
                    placeholder="input {}".format(_),
                )
                for _ in ALLOWED_TYPES
            ]
            + [html.Div(id="out-all-types")]
        )

    ])

])


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run_server(debug=True)
