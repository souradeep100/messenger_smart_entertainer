# coding: utf-8

import warnings
import os
from flask import Flask, request
from subprocess import call
import chatbot
import messenger

app = Flask(__name__)

FACEBOOK_TOKEN = "page token generated on messenger page of facebook app dashboard"
bot = None

@app.route('/', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token', '') == 'the token for verification given during webhook':
        return request.args.get('hub.challenge', '')
    else:
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data()
    for sender, message in messenger.messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)

       # response = bot.respond_to(message)
        if "hi" in message:
            response ="hello: type 1:for play music 2: for youtube arijit singh"
            print "Outgoing to %s: %s" % (sender, response)
            messenger.send_message(FACEBOOK_TOKEN, sender, response)
        if "1" in message:
            response ="playing now"
            print "Outgoing to %s: %s" % (sender, response)
            call(["/usr/bin/rhythmbox-client","--play"])
            messenger.send_message(FACEBOOK_TOKEN, sender, response)
        if "2" in message:
            response ="playing arijit singh youtube"
            print "Outgoing to %s: %s" % (sender, response)
            call(["/usr/bin/google-chrome"," https://www.youtube.com/watch?v=Z7hD0TUV24c"])
            messenger.send_message(FACEBOOK_TOKEN, sender, response)

    return "ok"

if __name__ == '__main__':
    # Suppress nltk warnings about not enough data
    warnings.filterwarnings('ignore', '.*returning an arbitrary sample.*',)

    if os.path.exists("corpus.txt"):
        bot = chatbot.Bot(open("corpus.txt").read())

    app.run(port=8080, debug=True)
