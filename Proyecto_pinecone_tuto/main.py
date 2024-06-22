#libreria necesarias

#!pip install -U sentence-transformers
#!pip install chromadb


import pandas as pd
from sentence_transformers import SentenceTransformer, util

import subprocess

# Ejecutar el comando desde Python para descargar en una ruta el csv de la informacion
subprocess.call(["gsutil", "-m", "cp", "-r", "gs://zaia-health-dev_pocs/etl/typeSideEffect", "C:\Developer_1.0\Proyecto_GCP\\"], shell=True)

#creamos una variable y le asignamos el CSV
df = pd.read_csv('C:\\Developer_1.0\\Proyecto_GCP\\typeSideEffect\\2024_03_07_1709771913793_0.csv')


# Divide la columna "comment" por coma y expandela en dos nuevas columnas
nuevos_comentarios = df['comment'].str.split(',', expand=True)

# Añade las nuevas columnas al DataFrame (opcional)
df = pd.concat([df, nuevos_comentarios], axis=1)

#elimina colummnas que se crearon de mas
df = df.drop([2,3,4,5,6,7,8,9,10],axis=1)

#renombra las 2 columnas nuevas
df = df.rename(columns={0: 'ingles', 1: 'español'})

#modifica la columna ingles y la normaliza
df['ingles'] = df['ingles'].str.strip('{')
df['ingles'] = df['ingles'].str.replace('["]', '', regex=True)
df['ingles'] = df['ingles'].str[4:]

#modifica la columna español y la normaliza
df['español'] = df['español'].str.strip('}')
df['español'] = df['español'].str.replace('["]', '', regex=True)
df['español'] = df['español'].str[5:]

#elimina la columna vieja
df = df.drop('comment', axis=1)

#concatena las columnas qye convertiremos a embbeding
df['text'] = df.apply(lambda x : x['ingles']+' '+x['español'], axis=1)

#cargamos el modelo de sentencetransformer
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#cargamos los emmbedins creados a la variable embbeding
embeddings = model.encode(df['text'],batch_size=64,show_progress_bar=True)

#creamos otra columna llamada ids con los id
df['embeddings'] = embeddings.tolist()
df['ids'] = df.index
df['ids'] = df['ids'].astype('str')


#se usa este de sentence y asi se declara el modelo
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name = 'all-MiniLM-L6-v2')

#cargamos la base de dato en la ruta que escojemos en local
chroma_client = chromadb.Client()
client_persistent = chromadb.PersistentClient(path= '/content/data_embeddings/')

#creamos una coleccion dentro de la base de datos en la variable db
db = client_persistent.create_collection(name = 'prueba23',embedding_function=sentence_transformer_ef)


#se cargan los datos embeddings de df a la base de datos croma
batch_size = 5000  # Tamaño de lote deseado

# Obtener el número total de elementos
total_elements = len(df)

# Iterar sobre los datos en lotes más pequeños
for i in range(0, total_elements, batch_size):
    batch_ids = df['ids'].tolist()[i:i+batch_size]
    batch_embeddings = df['embeddings'].tolist()[i:i+batch_size]
    batch_metadatas = df.drop(['ids','embeddings', 'español'], axis=1).iloc[i:i+batch_size].to_dict('records')
    
    # Agregar el lote a la base de datos
    db.add(ids=batch_ids, embeddings=batch_embeddings, metadatas=batch_metadatas)

results = db.query(
    query_texts=['dolor en extremidad superior'],
    n_results=2
)

results