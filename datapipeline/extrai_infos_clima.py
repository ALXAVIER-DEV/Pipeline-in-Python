import os 
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

# range de datas

dt_ini = datetime.today()
dt_fim = dt_ini + timedelta(days=7)

# ajustando as datas
dt_ini = dt_ini.strftime('Y%-%m-%d')
dt_fim = dt_fim.strftime('Y%-%m-%d')

city = 'Boston'
key = 'GTPH5E38DT6CY2MVTRQG882L6'
      


URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
    f'{city}/{dt_ini}/{dt_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())

file_path = '/home/alxavier/Documents/datapipeline/semana={dt_ini}/'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime','description', 'icon']].to_csv(file_path + 'condicoes.csv')


