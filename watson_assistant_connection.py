from watson_developer_cloud import AssistantV1

class WatsonAssistantConnection:
    __instance = None
    def get(self):
        if WatsonAssistantConnection.__instance is None:
            WatsonAssistantConnection.__instance = AssistantV1(
                version='2018-09-20',
                url='https://gateway.watsonplatform.net/assistant/api',
                username='95728531-51ee-436c-8a91-bea487036106',
                password='dd3O74rzB6fT'
            )
        return WatsonAssistantConnection.__instance
