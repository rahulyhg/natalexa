# natalexa.py
# Margaret Gorguissian
# 8/16/2017

import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import astro.py

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
    return ## get_new_fact() #TO CHANGE

@ask.intent(#'GetNewFactIntent') #TO CHANGE
def get_new_fact(): #TO CHANGE
    # EDIT
    return #TO CHANGE

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    return question(help_text).reprompt(help_text)

@ask.intent('AMAZON.StopIntent')
def stop():
    bye_text = render_template('bye')
    return statement(bye_text)

@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
