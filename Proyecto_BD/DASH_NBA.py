import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import consultas as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

con = Connection()
con.openConnection()



con.closeConnection()

