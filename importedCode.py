# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:30:28 2022

@author: 91995
"""

import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "DASHBOARD"

app.layout = html.Div(style={'backgroundColor': '#000'}, children=[

    dbc.Container([

        dbc.Row([
            html.Div("WORDOMINATOR", style={'fontSize': 25, 'color': '#000', 'textAlign': 'center'})

        ])

    ])

])
if __name__ == "__main__":
    app.run_server(debug=True)
