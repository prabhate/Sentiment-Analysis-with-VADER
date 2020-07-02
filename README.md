# Sentiment-Analysis-with-VADER
A simple web app that determines whether a piece of code is positive,neutral or negative in mood.

The model is written in the model.py file and stored in pickle format as model.pkl.

whenever a new user input is sent to the form in the webpage , it is sent to the flask application(app.py).\
1)model is loaded in app.py\
2)the user input is sent as an input to the model and sentiment scores are received as output\
3)it is then displayed using the webpage
