# Chatterbot, Tinker GUI and Flask Web Deployment

## Initial Setup:

pip install chatterbot <br>
pip install chatterbot-corpus<br>
pip install Flask<br>
pip install tk<br>

or

pip install -r requirements.txt

## Chatterbot implementation
This is a simple chatterbot implementation.  We use the chatterbot.corpus.english for training data, and the training result was saved in sqlit database.  

You may redo the taring using different corpus. See [ChatterBot documentation](https://chatterbot.readthedocs.io/en/stable/setup.html) for detail.

## tkinter GUI
<img src='/img/Tkinter.png' style='width: 300px'/>

Python code for the tkinter GUI was based on [this code](https://github.com/python-engineer/python-fun/blob/master/chatbot-gui/app.py)

## Web deployment with Flask and Javascript
<img src='/img/ChatterBot.png' style='width: 300px'/>

We deploy the chatbot within Flask app with jinja2 template. Flask & JavaScript code was based on [this repo](https://github.com/python-engineer/chatbot-deployment).

Run app.py. Then in your browser, navigate to <localhost:5000>.  If necessary, use Ctrl + F5 to hard reload the page.  On Apple / MAC, the shortcut is Command + R.
