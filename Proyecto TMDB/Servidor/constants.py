#Data Base Constants
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "ZnvzV4whRfi4xpQw"
MYSQL_DB = "bd_tfg"

#Server constanst
HOSTNAME = "localhost"
SERVERPORT = 8080

#Data Files Constants

DATA_FOLDER = "dataset/"
MODEL_FOLDER = "modelos/"
EMBEDDING_FOLDER = "embeddings/"

#Data Files names

ACTORS_EMBEDDING = "embeddings-actors.pkl"
TITLE_EMBEDDING = "embeddings-title.pkl"
OVERVIEW_EMBEDDING = "embeddings-overviews.pkl"

#Model names
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

#ENUM
class EMBEDDING:
    TITLE = 1
    OVERVIEW = 2
    ACTORS = 3