import requests

sheety_endpoint = "https://api.sheety.co/d60c84605824c2934f2f0b310fd6024f/flightDeals/prices"
sheety_users_endpoint = "https://api.sheety.co/d60c84605824c2934f2f0b310fd6024f/flightDeals/users"
sheety_token = "Andrew"
sheety_name = "price"

class DataManager:

    def __init__(self):

        self.token = sheety_token
        self.prices_endpoint = sheety_endpoint
        self.users_endpoint = sheety_users_endpoint
        self.authorization = f"Bearer {sheety_token }"
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        headset = {
            "Authorization": self.authorization
        }
        response = requests.get(url=self.prices_endpoint, headers = headset)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headset = {
                "Authorization": self.authorization
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,headers = headset
            )
            print(response.text)

    def get_customer_emails(self):
        headset = {
            "Authorization": self.authorization
        }
        response = requests.get(url=self.users_endpoint,headers = headset)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

