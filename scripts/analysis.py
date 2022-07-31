from pymongo import MongoClient
from textblob import TextBlob
import statistics


def get_data(coin_symbol):
    cluster = MongoClient('mongodb+srv://user:pass@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
    database = cluster['data']
    google_collection = database['google_news']

    results = google_collection.find({'coin symbol':coin_symbol})

    if not results:
        print('no data')

    return results



def analyze(results):
    scores = []
    for data in results:
        title_score = TextBlob(data['article title']).sentiment
        description_score = TextBlob(data['article description']).sentiment
        scores.append(title_score[0])
        scores.append(description_score[0])
    
    filtered = []
    for score in scores:
        if score > 0.25 or score < -0.25:
            filtered.append(score)

    score = statistics.mean(filtered)
    stringScore = str(score)

    return stringScore
        
