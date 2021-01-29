# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from typing import Any, Dict, List, Text, Optional

from rasa_sdk.events import SlotSet, EventType

class ActionCheckAccountBalance(Action):
	def name(self) -> Text:
		return "action_check_account_balance"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[EventType]:

		dispatcher.utter_message("Your account balance is $1.")
		return []


class ActionUpdateInformation(Action):
	def name(self) -> Text:
		return "action_update_information"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[EventType]:

		payment_amount = next(tracker.get_latest_entity_values("amount-of-money"), None)

		return [SlotSet('payment_amount', payment_amount), SlotSet("payment_date", time)]


class ValidateCCPaymentForm(FormValidationAction):
	def name(self)->Text:
		return "validate_cc_payment_form"

	def validate_payment_amount(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]
	) -> Dict[Text, Any]:

		if value > 0:
			return {"payment_amount": value}
		else:
			return {"payment_amount": None}


	def validate_source_account(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]
	) -> Dict[Text, Any]:

		return {"source_account": value}

	def validate_destination_account(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]
	) -> Dict[Text, Any]:

		return {"destination_account": value}

	def validate_payment_date(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]
	) -> Dict[Text, Any]:

		return {"payment_date": value}

	def validate_confirm(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]
	) -> Dict[Text, Any]:

		if value == 'yes':
			return {"confirm": value}
		else:
			return {"confirm": None}


