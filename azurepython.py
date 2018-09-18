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
    return render_template("index.html")
@app.route('/get')
#@app.route('/',methods = ['GET'])
#def home():
def get_bot_response():
    userText = request.args.get('msg')
    lot = re.findall('\d+', userText)
    # print(lot)
    y = userText.split()
    #texts = [[word.lower() for word in y] for text in y]
    texts = [word.lower() for word in y]
    print (texts)
    #z = y.lower() #to lower the alphabet
    #print (y)
    k = "bmi"
    print (k)
    if any(word in k for word in texts):
        print(123)
        response = 'enter weight(kg) and height(cm)'
        return str(response)

    #lot = re.findall('\d+', userText)
    #print(lot)
    elif len(lot) == 2:
        print('condition check',lot)
        w = float(lot[0])
        print (w)
        h= float(lot[1])
        h = h/100
        print (h)
        bmi = float(w/(h*h))
        bmi = round(bmi,2)
        print(bmi)
        if (bmi<=18.5):
            a = 'underweight'
            i=float(19)*(float(h*h))
            print(i)
    #logger.info('Got the values2')
            r = int(i) - int(w)
            i = round(i,2)
    #logger.info('Start reading database')
            speech = 'Your bmi is {} and you are {} So your ideal weight should be {}kg and you have to gain {}kg'.format(bmi, a,i,r)
            return str(speech)
        elif (bmi>18.5 and bmi<24.9):
            a = 'healthy'
            speech = 'Your bmi is {} and you are {}'.format(bmi, a)
            return str(speech)
    #logger.info('Got the values3')
        elif (bmi>25.0 and bmi<29.9):
                a ='overweight'
                i = float(25) * (float(h * h))
                print(i)
                r = int(w) - int(i)
                i = round(i, 2)
                speech = 'Your bmi is {} and you are {} So your ideal weight should be {}kg and you have to reduce {}kg'.format(bmi, a, i,r)
                return str(speech)
    #logger.info('Got the values4')
        else:
            a = 'obese'
            i = float(25) * (float(h * h))
            print(i)
            r = int(w) - int(i)
            i = round(i, 2)
    #logger.debug('Records: %s', i)
    #logger.info('Got the values5')
            speech = 'Your bmi is {} and you are {} So your ideal weight  should be {}kg and you have to reduce {}kg'.format(bmi, a, i,r)
            return str(speech)
       # bmi1 = 'Your bmi is {}'.format(bmi)
    '''else:
          speech = 'you have to enter two values'
          return str(speech)'''
    #elif not lot:
    #print (lot)
    #elif not lot:
    if any(word in k for word in y):
        print(456)
    #if userText.strip()!='bmi':
             #return str(english_bot.get_response(userText))
             #speech ='{}' .format(english_bot.get_response(userText))
             #return str(speech)

    #elif  userText.strip()=='bmi':
    #elif  userText.strip()=='bmi':
    #if any(word in k for word in y):
     #   print(789)
       # response = 'enter weight(kg) and height(cm)'
        #return str(response)

if __name__ == "__main__":
    app.run()
