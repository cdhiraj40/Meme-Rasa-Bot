# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import random 

class ActionShowMeme(Action):

    def name(self) -> Text:
        return "action_show_meme"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        random_num = random.randint(0, 99)
        print(random_num)

        response = requests.get("https://api.imgflip.com/get_memes")

        response = response.json()

        url = response["data"]["memes"][random_num]["url"]
        print(url)
        dispatcher.utter_message(text=url)

        return []
