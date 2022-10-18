# -*- coding: utf-8 -*-

# import dash-core, dash-html, dash io, bootstrap
from dash import html
from dash import dcc, dash_table
from dash.dependencies import Input, Output, State

from PIL import Image
# Dash Bootstrap components
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import base64
import io
# Navbar, layouts, custom callbacks
#from layouts import profilLayout ,teamLayout

# Import custom data.py
from data import *



# Import app
from app import app
# Import server for deployment
from app import srv as server
# Import data from data.py file



# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
logo1=Image.open("assets/logo2.png")
sidebar = html.Div(
    [
        #html.H2("AI MATCH", className="display-5"),
        html.Img(src=logo1, height="200",width="230"),
        html.H2("Data Explorer", className="display-5"),
        html.Hr(),
        dbc.Nav(
            [dbc.NavLink("Home", href="/", active="exact")],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Analyse", href="/Analyse", active="exact"),
                dbc.NavLink("Profiles types des participants", href="/Profiles", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        html.H2("Machine Learning Analysis", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Projections and Regression", href="/projection", active="exact"),
                dbc.NavLink("Tester vos données !", href='/tester', active='exact')
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

# Sidebar layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

logo=Image.open("assets/logo.png")

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/':
        return [html.Div([dcc.Markdown('''
            ###  TROUVER UNE PERSONNE PARFAITEMENT COMPATIBLE
            
            Cette application est un projet de Easy Date réalisé par [Haidara Fatimetou, KIEMDE Christelle, DUBRULLE Pierre] 
            à l'aide de Dash de Plotly,
            les composants Dash Bootstrap de faculty.ai, Pandas,et des fonctions personnalisées. 
    
            Easy Date est une société d'événementiel qui organise des speed dating.
            Pour s’inscrire, une personne doit remplir un formulaire avec différentes
            informations sur elle et ses attentes. L’entreprise récolte ainsi les données et
            organise différentes vagues de speed dating.
            
            Lors d’une session, un participant rencontre plusieurs personnes. A l’issue de
            chaque rencontre, il décide si Oui/Non la personne veut revoir un ou des
            coups de cœur.
            
            Le problème, c’est le faible taux de match qui fait perdre beaucoup de temps
            à l’entreprise et donc de l’argent.
            
            L’équipe de data scientist de l’entreprise doit donc réfléchir à un modèle
            permettant de prédire si deux personnes vont matcher selon le formulaire
            complété préalablement de la rencontre.
            
            Cela fait des mois qu’ils planchent sur le projet, ils ont déjà calculé un score de
            similarité entre deux participants en se basant sur leurs réponses aux
            questionnaires. 
            Cependant, ce score ne semble pas fiable et l’entreprise
            souhaiterait un modèle de scoring plus performant pour prédire si l’amour va
            opérer entre deux personnes.
            
            C’est la raison pour laquelle le projet AI match a vu le jour !
        ''')],className='home',style={'text-align':'center'}),
        
        html.Div(html.Img(src=logo), style={'text-align':'center'}),
        
        
        
        ]
    elif pathname == '/Analyse':
        return [html.Div([
    
    ### Graphs of Historical  statistics ###
    dbc.Row(dbc.Col(html.H3(children='Analyse', style={'text-align':'center', 'font-size':'100px','font-family':'nunito','background-color':'red', 'background-image':'conic-gradient(#f3ec78, #af4261)', 'background-size':'100%','background-repeat':'repeat','-webkit-background-clip':'text','-webkit-text-fill-color':'transparent','-moz-background-clip':'text', '-moz-text-fill-color':'transparent', 'font-weight':'900'}))),
    
    dcc.Graph(
     
       figure=age()
   ),

   dcc.Graph(

    figure = match_genre()
   ),

   dcc.Graph(

    figure = goout()
   ),

   dcc.Graph(

    figure = activite()
   ),

   dcc.Graph(

    figure = income()
   )
])]

 
    elif pathname == '/Profiles':
        return [html.Div(children=[
                html.H1(children='Profils types des participants', style={'text-align':'center', 'font-size':'100px','font-family':'nunito','background-color':'red', 'background-image':'conic-gradient(#f3ec78, #af4261)', 'background-size':'100%','background-repeat':'repeat','-webkit-background-clip':'text','-webkit-text-fill-color':'transparent','-moz-background-clip':'text', '-moz-text-fill-color':'transparent', 'font-weight':'900'}),
                html.Div(children=[
                    html.Img(src='assets/profil.png', style={'position':'relative', 'top':'200px', 'height':'100px'}),
                    html.H1(children='27 ans', style={'position':'relative','left':'150px','top':'100px', 'font-size':'25px'}),
                    html.H1(children='Études de finance', style={'position':'relative','left':'150px','top':'105px','font-size':'25px'}),
                    html.H1(children='Caucasien', style={'position':'relative','left':'150px','top':'110px','font-size':'25px'}),
                    html.H1(children='Ingénieur', style={'position':'relative','left':'150px','top':'115px','font-size':'25px'}),
                    html.H1(children='46 274$/mois', style={'position':'relative','left':'150px','top':'120px','font-size':'25px'}),
                    html.H1(children='Aime le sport/les livres/les films/la musique', style={'position':'relative','left':'150px','top':'125px','font-size':'25px'}),
                    html.H1(children='1 date/mois', style={'position':'relative','left':'150px','top':'130px','font-size':'25px'}),
                    html.H1(children='2 sorties/semaine', style={'position':'relative','left':'150px','top':'135px','font-size':'25px'})
                ], style={'float':'left', 'width':'40%'}),

                html.Div(children=[
                    html.Img(src='assets/femelle.png', style={'position':'relative', 'top':'200px', 'height':'100px'}),
                    html.H1(children='26 ans', style={'position':'relative','left':'150px','top':'100px','font-size':'25px'}),
                    html.H1(children='Études de finance', style={'position':'relative','left':'150px','top':'105px','font-size':'25px'}),
                    html.H1(children='Sud-américain/Hispanique', style={'position':'relative','left':'150px','top':'110px','font-size':'25px'}),
                    html.H1(children='Ingénieur', style={'position':'relative','left':'150px','top':'115px','font-size':'25px'}),
                    html.H1(children='44 577$/mois', style={'position':'relative','left':'150px','top':'120px','font-size':'25px'}),
                    html.H1(children='Aime les diners/les musées/les films/les arts', style={'position':'relative','left':'150px','top':'125px','font-size':'25px'}),
                    html.H1(children='1 date/mois', style={'position':'relative','left':'150px','top':'130px','font-size':'25px'}),
                    html.H1(children='2 sorties/semaine', style={'position':'relative','left':'150px','top':'135px','font-size':'25px'})
                ], style={'float':'left','width':'40%'})
                ], style={'position':'absolute', 'top':'10px','left':'290px', 'width':'90%'})]

    elif pathname == '/tester':
        return [html.Div([
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
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])]


        

    else:
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), sep=';', on_bad_lines='skip')
    except Exception as e:
        print(e)
        return html.Div([
            "Une erreur s'est produite."
        ])

    return html.Div([
        html.H5(filename),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': x, 'id': x} for x in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:500] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children








# Call app server
if __name__ == '__main__':
    # set debug to false when deploying app
    app.run_server(debug=True)
