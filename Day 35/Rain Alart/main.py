import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b09bd2e3e774dd208908c8d937c162f8"
account_sid = "AC5c73a07e65c32ea6da3b23a0602e12f4"
auth_token = "31958c381a8ce9c914b94918a94f2bb7"


weather_params = {
    "lat": 48.1374,
    "lon": 11.5755,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+15075744375",
        to="+380969638363"
    )
    print(message.status)