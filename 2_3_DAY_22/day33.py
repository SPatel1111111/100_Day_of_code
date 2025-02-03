import requests
import datetime

MY_LAT=20.593683
MY_LNG=78.962883

#iss API

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data =response.json()
# print(data)
#
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
#
# iss_position =(longitude,latitude)
# print(iss_position)


#sunset and sunset time

parameters ={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response=requests.get(" https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()

sunrise=data["results"]["sunrise"].split("T")[1].split(":")
sunset=data["results"]["sunset"].split("T")[1].split(":")

print(f"sunrise time {sunrise[0]}:{sunrise[1]}")
print(f"sunset time {sunset[0]}:{sunset[1]}")
now=datetime.datetime.now()
print(f"Now time {now.time()}")