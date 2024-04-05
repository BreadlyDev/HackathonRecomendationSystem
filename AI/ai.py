# import pandas as pd
# import pickle
#
# import nltk
# from nltk.stem.porter import PorterStemmer
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# df = pd.read_csv('spotify_millsongdata.csv')
# df = df.sample(40000).drop('link', axis=1).reset_index(drop=True)
#
# # Text Cleaning/ Text Preprocessing
# df['text'] = df['text'].str.lower().replace(r'^\w\s', ' ').replace(r'\n', ' ', regex = True)
# nltk.download('punkt')
# stemmer = PorterStemmer()
#
# def token(txt):
#     token = nltk.word_tokenize(txt)
#     a = [stemmer.stem(w) for w in token]
#     return " ".join(a)
#
# # token("you are beautiful, beauty")
#
# df['text'].apply(lambda x: token(x))
# tfid = TfidfVectorizer(analyzer='word', stop_words='english')
# matrix = tfid.fit_transform(df['text'])
# similar = cosine_similarity(matrix)
#
#
# # Recommender Function
# def recommender(song_name):
#     idx = df[df['song'] == song_name].index[0]
#     distance = sorted(list(enumerate(similar[idx])), reverse=True, key=lambda x: x[1])
#     song = []
#     for s_id in distance[1:5]:
#         song.append(df.iloc[s_id[0]].song)
#     return song
#
#
# pickle.dump(similar, open('similarity', 'wb'))
# pickle.dump(df, open('df', 'wb'))


import os
import pickle

# Загрузка сохраненных объектов

current_dir = os.path.dirname(os.path.abspath(__file__))

# Загрузка сохраненных объектов с указанием абсолютного пути
similar = pickle.load(open(os.path.join(current_dir, 'similarity'), 'rb'))
df = pickle.load(open(os.path.join(current_dir, 'df'), 'rb'))

# Ваш код, использующий df и similar
# Например, в функции recommender:

# Recommender Function
def recommender(song_name):
    idx = df[df['song'] == song_name].index[0]
    distance = sorted(list(enumerate(similar[idx])), reverse=True, key=lambda x: x[1])
    song = []
    for s_id in distance[1:5]:
        song.append(df.iloc[s_id[0]].song)
    return song