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

english_bot = ChatBot("GUI Bot", read_only=True,
                      preprocessors=[
                          'chatterbot.preprocessors.clean_whitespace'
                      ],

                      logic_adapters=[
                                         {
                                             'import_path': 'chatterbot.logic.BestMatch',
                                             "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                                             "statement_comparison_function1": "chatterbot.comparisons.SentimentComparison",
                                             "statement_comparison_function2": "chatterbot.comparisons.SynsetDistance",
                                             "response_selection_method": "chatterbot.response_selection.get_random_response"
                                         },
                                     # {
                                     # 'import_path':'chatterbot.logic.TimeLogicAdapter',
                                     # 'threshold': 0.50
                                     # },
                                     # {
                                     # 'import_path':'chatterbot.logic.MathematicalEvaluation',
                                     # 'threshold': 0.50
                                     # },

{
        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        'threshold': 0.85,
        'default_response': 'I am sorry, but I do not understand.'
        }
                            # "chatterbot.logic.BestMatch"

        ],
		storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
		input_adapter="chatterbot.input.VariableInputTypeAdapter",
        output_adapter="chatterbot.output.OutputAdapter",
		filters=['chatterbot.filters.RepetitiveResponseFilter'],
        database="database4"
      )

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application Running!'
    #return render_template("index.html")

if __name__ == "__main__":
    app.run()
