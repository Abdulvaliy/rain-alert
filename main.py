import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key_goes_here"
account_sid = "your_account sid can be here"
auth_token = "your auth token in twilio, or other web-site"

my_latitude = 41.2995
my_longitude = 69.2401


parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly = weather_data["hourly"]

will_rain = False

for hour in hourly[:12]:
    weather_condition = hour["weather"][0]["id"]  # #### weather conditions #####
    if int(weather_condition) < 700:  # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
        will_rain = True

if will_rain:
    # print("Bring an umbrella. It's going to rain! ☔ ")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today! Remember to bring an umbrella ☔ ",
            from_="+your twilio number e.g. +178...",
            to="registered phone number e.g. +998..."
        )
    print(message.status)
