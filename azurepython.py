# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 12:50:41 2018

@author: DELL
"""



from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import re
from flask import make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application Running!'
    #return render_template("index.html")

if __name__ == "__main__":
    app.run()
