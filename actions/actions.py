# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import re
import webbrowser
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


class ActionUserDetails(Action):

    def name(self) -> Text:
        return "action_user_details_form"
    
    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
    #     name = tracker.get_slot("name")
    #     if not name:
    #         dispatcher.utter_message(text="Please provide your name")
    #     else:
    #         dispatcher.utter_message(text="Your name is {}".format(name))
    #     return []

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        required_slots = ["name", "email", "phone"]
        for slot_names in required_slots:
            if tracker.slots.get(slot_names) is None:
                #ekhane slot name gula required slot er moddhe ache kina check korchi by requesting user to fill
                return [SlotSet("requested_slot", slot_names)]
        # if all slots are filled, return empty list
        return [SlotSet("requested_slot", None)]

class ActionUserAccountsForm(Action):
    def name(self) -> Text:
        return "action_user_accounts_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        required_slots = ["account_number", "nation"]
        for slot_names in required_slots:
            if tracker.slots.get(slot_names) is None:
                #ekhane slot name gula required slot er moddhe ache kina check korchi by requesting user to fill
                return [SlotSet("requested_slot", slot_names)]
        # if all slots are filled, return empty list
        return [SlotSet("requested_slot", None)]
                         
            

# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
#     def run(self,
#             dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: DomainDict
#             ) -> List[Dict[Text, Any]]:
#             name = tracker.get_slot("name")
#             email = tracker.get_slot("email")
#             phone = tracker.get_slot("phone")

#             dispatcher.text("Thanks for submitting your details, Dear {}. We will contact you soon at {}".format(name, email))

#             return [SlotSet("requested_slot", None)]
        

class ValidateUserForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_details_form"

    def validate_name(self, 
                    slot_value: Any, 
                    dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: DomainDict) -> Dict[Text, Any]:
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Name must be more than 3 characters")
            return {"name": None}
        else:
            return {"name": slot_value}

    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def validate_email(self,
                        slot_value: Any,
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: DomainDict) -> Dict[Text, Any]:
        if re.match(self.email_regex, slot_value):
             dispatcher.utter_message(text="Great! Your email is valid.")
             return {"email": slot_value}
        else:
             dispatcher.utter_message(text="Please provide a valid email")
             return {"email": None}

    
    def validate_phone(self, 
                        slot_value: Any, 
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: DomainDict) -> Dict[Text, Any]:
        if len(slot_value) != 11:
            dispatcher.utter_message(text="Please provide a valid phone number")
            return {"phone": None}
        else:
            return {"phone": slot_value}
        
class ValidateUserAccountsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_accounts_form"

    def validate_account_number(self, 
                    slot_value: Any, 
                    dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: DomainDict) -> Dict[Text, Any]:
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Account number must be more than 10-12 characters")
            return {"account_number": None}
        else:
            return {"account_number": slot_value}

    
    def validate_nation(self, 
                        slot_value: Any, 
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: DomainDict) -> Dict[Text, Any]:
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Please provide a nationality based on our criterias")
            return {"nation": None}
        else:
            return {"nation": slot_value}

class VideoPlayer(Action):
    def name(self) -> Text:
        return "action_play_video"
    

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        
        video_url = "https://www.youtube.com/watch?v=ykeamfE0-g4"
        dispatcher.utter_message(text="Please watch this video: {} and wait -_--_-_-_-_-_-_-".format(video_url))
        webbrowser.open(video_url)
        return []
