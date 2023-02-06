import requests
from pprint import pprint

SHEETY_ENDPOINT = 'https://api.sheety.co/ab7ad54602478220de6df55a4f8e952c/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destitation_data(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.destination_data = self.data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            self.response_update = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(self.response_update.text)




# data_manager = DataManager()
# data_manager.get_destitation_data()
