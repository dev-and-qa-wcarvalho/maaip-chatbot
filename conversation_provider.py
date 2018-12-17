from flask import render_template

class ConversationProvider:
    def __init__(self, watson_assistant_connection):
        self.__watson_assistant_connection = watson_assistant_connection
        self.__workspace_id = '86c16e78-0759-4bf5-a777-b431dc091c03'
    def send_message(self, question):
        response = self.__watson_assistant_connection.get().message(workspace_id=self.__workspace_id, input={'text': question}).get_result()['output']['generic']
        if len(response) > 0:
            return render_template('index.html', response=response[0]['text'])
        return render_template('index.html')
