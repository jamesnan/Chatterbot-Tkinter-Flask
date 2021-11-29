# Chatterbot with Tinker GUI and Flask Web Deployment

## Initial Setup:
pip install chatterbot <br>
pip install chatterbot-corpus<br>
pip install Flask<br>
pip install tk<br>

or

pip install -r requirements.txt

## [chatterbot implementaiton]("chatbot_corpus.py")
This is a simple chatterbot implementation.  We use the chatterbot.corpus.english for training data, and the training result was saved in sqlit database.  You may redo the traing using different corpus. 

## tkinter GUI
<img src='/img/tkinter.png' style='width: 600px'/>

Python code for the tkinter GUI was based on [This code](https://github.com/python-engineer/python-fun/blob/master/chatbot-gui/app.py)

## Web deployment with Flask and Javascript
<img src='/img/ChatterBot.png' style='width: 600px'/>

We deploy the chatbot within Flask app with jinja2 template. Flask & Javascript code was based on [This repo](https://github.com/python-engineer/chatbot-deployment).

Run app.py, then in your browser navigate to <localhost:5000>.  If nessasry, use Ctrl + F5 to hard reload the page.  On Apple / MAC, the shortcut is Command + R.


