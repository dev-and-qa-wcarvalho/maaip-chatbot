from watson_assistant_connection import WatsonAssistantConnection
from dialog_creator import DialogCreator
from conversation_provider import ConversationProvider
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    return DialogCreator(WatsonAssistantConnection())\
    .add_intent(request.form['intent'])\
    .add_question(request.form['questionToTip'])\
    .add_tip(request.form['tip'])
    return 'Dica adicionada com sucesso!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return ConversationProvider(WatsonAssistantConnection()).send_message(request.form['question'])
    return render_template('index.html')

app.run(port=8081)