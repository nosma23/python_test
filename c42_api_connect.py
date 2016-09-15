import requests

api_token = "d667e51ab738c8e82179aa14bf4340a4aefd69f5"

event_id = "c96a8bb00d8b39d410ea459591e8db40_14734093154132"

api_endpoint = "https://demo.calendar42.com/api"


def get_event_details():
	endpoint = '/v2/events/c96a8bb00d8b39d410ea459591e8db40_14734093154132/'
	final_api_endpoint = api_endpoint + endpoint
	auth = ("Token d667e51ab738c8e82179aa14bf4340a4aefd69f5", "")
	params = {
		"event_ids": event_id,
		"title": "HOME",
	}
	r = requests.get(final_api_endpoint, auth=auth, params=params)
	return r.json()


def get_event_subscriptions():
	endpoint = '/v2/event-subscriptions/?event_ids=c96a8bb00d8b39d410ea459591e8db40_14734093154132'
	final_api_endpoint = api_endpoint + endpoint
	auth = ("Token d667e51ab738c8e82179aa14bf4340a4aefd69f5", "")
	params = {
		"event_ids": event_id,
		"first_name": "Ella",
        "last_name": "Bartledan",
        "user_id": "42abc42de"
	}
	r = requests.get(final_api_endpoint, auth=auth, params=params)
	return r.json()

