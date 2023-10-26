import pandas as pd
import pickle
from sqlalchemy import create_engine
from sqlalchemy import text
import constants
import pymysql
import os


def listToString(list):
    str1 = "["
    isNotFirst = False

    for elem in list:
        if isNotFirst:
            str1 += ', '
        isNotFirst = True

        str1 += str(elem)
    return str1 + "]"

def createPrimaryKeyQuery(table, column_name):
      return """ALTER TABLE {table} 
CHANGE COLUMN {column_name} {column_name} BIGINT NOT NULL ,
ADD PRIMARY KEY ({column_name});""".format(table = table, column_name = column_name);

def createFulltextIndexQuery(table, column_name, index_name):
      return """CREATE FULLTEXT INDEX {index_name}
ON {table}({column_name});""".format(table = table, column_name = column_name, index_name=index_name);


MYSQL_HOST = constants.MYSQL_HOST
MYSQL_PORT = constants.MYSQL_PORT
MYSQL_USER = constants.MYSQL_USER
MYSQL_PASSWORD = constants.MYSQL_PASSWORD
MYSQL_DB = constants.MYSQL_DB

engine = create_engine("mysql+pymysql://" + MYSQL_USER + ":" + MYSQL_PASSWORD + "@" + MYSQL_HOST + ":" + str(MYSQL_PORT) + "/" + MYSQL_DB)

print("Conexion con la base de datos creada correctamente.")


genres_file_path = "Datos/genres_ids.csv" #@param {type:"string"}

df_genres = pd.read_csv(genres_file_path)
df_genres.to_sql('genres', con=engine, if_exists='replace', index = False)

print("Tabla de generos creada correctamente.")

with engine.connect() as connection:
      print("Creando claves primarias...")
      connection.execute(text(createPrimaryKeyQuery('genres', 'genre_id')))

print("Tabla de generos configurada correctamente.")





movies_genres_file_path = "Datos/movies_genres.csv" #@param {type:"string"}

df_moviesGenres = pd.read_csv(movies_genres_file_path)
df_moviesGenres.to_sql('movies_genres', con=engine, if_exists='replace', index = False)

print("Tabla de películas-generos configurada correctamente.")

with engine.connect() as connection:
      print("Creando claves primarias...")
      connection.execute(text(createPrimaryKeyQuery('movies_genres', 'id_movie')))





movies_file_path = "Datos/dataset.csv" #@param {type:"string"}
similarity_Matrix_file_path = "Datos/similarity_matrix.pkl" #@param {type:"string"}

print("Cargando Dataset de Peliculas...")
df = pd.read_csv(movies_file_path)
df['id'] = range(0, len(df))

print("Cargando Matriz de similitudes...")
try:
  with open(similarity_Matrix_file_path, "rb") as fIn:
    resp = pickle.load(fIn)

    cosenos_biencoder = list()
    index_biencoder = list()

    for elem in resp['cosenos_biencoder']:
        cosenos_biencoder.append(listToString(elem.tolist()))
    
    for elem in resp['index_biencoder']:
        index_biencoder.append(listToString(elem.tolist()))

    df['index_biencoder'] = index_biencoder
    df['cosenos_biencoder'] = cosenos_biencoder

except Exception as e:
  raise e
else:
  print("Matriz de similitudes cargada correctamente.")

  print("Creando tabla de movies...")
  df.to_sql('movies', con=engine, if_exists='replace', index = False)

  print("Tabla de películas creada correctamente.")

  with engine.connect() as connection:
        print("Creando claves primarias...")
        connection.execute(text(createPrimaryKeyQuery('movies', 'id')))

        print("Creando FULLTEXT index...")
        connection.execute(text(createFulltextIndexQuery('movies', 'original_title', 'index_original_title')))
        connection.execute(text(createFulltextIndexQuery('movies', 'actors_string', 'index_actors_string')))
        connection.execute(text(createFulltextIndexQuery('movies', 'overview', 'index_overview')))
        print("Tabla de películas configurada correctamente.")