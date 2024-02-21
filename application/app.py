import dash
from dash import dcc
from dash import html

from database.config import server, db

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
