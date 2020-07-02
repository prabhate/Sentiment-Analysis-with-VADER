import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
pickle.dump(analyser, open('vader_model.pkl','wb'))