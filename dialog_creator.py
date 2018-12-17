class DialogCreator:
    def __init__(self, watson_assistant):
        self._watson_assistant = watson_assistant
        self._workspace_id = '86c16e78-0759-4bf5-a777-b431dc091c03'
        self._intent = ''
    def add_intent(self, intent):
        self._intent = intent.replace(' ', '-')
        try:
            self._watson_assistant.get().create_intent(workspace_id=self._workspace_id, intent=self._intent)
            return self
        except:
            return self
    def add_question(self, question):
        try:
            self._watson_assistant.get().create_example(workspace_id=workspace_id, intent=self._intent, text=question)
            return self
        except:
            return self
    def add_tip(self, tip):
        dialog = self._intent + '-dialog'
        try:
            self._watson_assistant.get().create_dialog_node(workspace_id=self._workspace_id, dialog_node=dialog, output={'text': tip})
            return self
        except:
            return self
