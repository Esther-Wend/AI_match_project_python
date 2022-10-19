# -*- coding: utf-8 -*-



# Import Pandas
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import KNNImputer
import dash
from dash import html
from dash import dcc
import plotly.express as px

font_family = 'nunito'






def activite():
  df = pd.read_csv("train.csv",sep=";")
  df_activite =df.iloc[:,45:62]# df.iloc[:,40:57]
  df_activite['sports'] = (df_activite['sports'] + df_activite['exercise'] + df_activite['hiking'] + df_activite['yoga'])/4

  df_activite.drop(columns=['exercise','hiking','yoga'],inplace=True)

  df_activite['tv'] = (df_activite['tv'] + df_activite['tvsports'])/2

  df_activite.drop(columns=['tvsports'], inplace=True)

  df_activite = pd.DataFrame(df_activite.mean(axis=0)*10).reset_index()
  df_activite.columns = ['activity','mean']

  fig_activites = px.bar(df_activite, x='activity', y='mean', 
                  labels={'activity':'Activités','mean':'Popularité (en %)'}, 
                  color='mean', 
                  color_continuous_scale=['#FEF9E7','#F8C471','#F39C12','#9C640C'])


  fig_activites.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'},yaxis_range=[0,100])

  fig_activites.update_layout(title={'text':'Popularités des activités', 'y':0.92, 'x':0.5, 'xanchor':'center','yanchor':'top'}, title_font_family=font_family, title_font_size=28)

  return fig_activites

def income():
  df = pd.read_csv("train.csv",sep=";")
  income = df[['income','age', 'gender']]
  income.replace({',':''}, regex=True, inplace=True)
  income['tranche'] = pd.cut(income['age'], bins=np.arange(15,55,5), labels=['17-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50'])

  income['gender'] = np.where(income['gender'] == 1, "Homme","Femme")

  income = pd.DataFrame(income.groupby(['tranche', 'gender'])['income'].median()).reset_index()

  income.dropna(inplace=True)

   

  mediane_h = (income.groupby('gender')['income'].median())[1]
  mediane_f = (income.groupby('gender')['income'].median())[0]


  fig_income = px.bar(income, x='tranche', y='income', color='gender', 
                  barmode="group", labels={'income': 'Salaire', 'tranche':'Tranches d\'âge'}, 
                  color_discrete_map={'Homme':'#FEF9E7', 'Femme':'#F39C12'}).add_hline(mediane_h).add_hline(mediane_f)

  fig_income.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})

  fig_income.update_layout(title={'text':'Salaire médian par tranche d\'age et par sexe', 'y':0.96, 'x':0.5, 'xanchor':'center','yanchor':'top'}, 
                      legend_title_text='Genre', title_font_family=font_family, title_font_size=28)

  return fig_income


def age():
  df = pd.read_csv("train.csv",sep=";")
  fig_age = px.histogram(df, x="age",title="Répartion de l'âge")
  fig_age.update_layout(bargap=0.2)
  fig_age.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
  fig_age.update_layout(title={'text':"Répartition de l'âge", 'y':0.92, 'x':0.5, 'xanchor':'center','yanchor':'top'},title_font_family=font_family, title_font_size=28)

  return fig_age

def goout():
  df = pd.read_csv("train.csv",sep=";")
  code_go = np.arange(1,8,1)
  label =["Plusieurs fois/semaine","Deux fois/semaines","Une fois/semaine","Deux fois/mois","Une fois/mois","Plusieurs fois/an","Presque jamais"]
  df['go_out'] = df['go_out'].replace(code_go, label)
  fig_goout = px.histogram(df, x="go_out",title='Répartition des fréquences (go_out) de participation', labels={'1':'Plusieurs fois/semaine', '2':'Deux fois/semaine','3':'Une fois/semaine','4':'Deux fois/mois','5':'Une fois/mois','6':'Quelques fois/année', '7':'Presque jamais'})
  fig_goout.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
  fig_goout.update_layout(title={'text':'Répartiton des fréquences (go_out) de participation', 'y':0.92, 'x':0.5, 'xanchor':'center','yanchor':'top'},title_font_family=font_family, title_font_size=28)
  fig_goout.update_xaxes(title='')
  return fig_goout

def match_genre():
  df = pd.read_csv("train.csv",sep=";")
  df['gender'] = np.where(df['gender'] == 1, "Homme","Femme")

  fig_matchgenre = px.box(df, x="gender", y="age",color="match",
      notched=True , # used notched shape
      title="Repartition de l'age en fonction du sexe selon le profile match",
      )
  fig_matchgenre.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
  fig_matchgenre.update_layout(title={'text':'Répartition de l\'âge en fonction du sexe et selon le match', 'y':0.92, 'x':0.5, 'xanchor':'center','yanchor':'top'},title_font_family=font_family, title_font_size=28)

  return fig_matchgenre



