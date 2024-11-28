import http.client
import json
import time
import threading

city = input("Enter the city to fetch fuel prices: ").strip()

def animate_loading():
    animation = ["|", "/", "-", "\\"]
    i = 0
    while not data_fetched:
        print(f"\rFetching data... {animation[i % len(animation)]}", end="")
        time.sleep(0.5)
        i += 1

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 4oNmb7dqK6ZA9NOD6CxZsI:3gZxeIb1CeC102fvqyUj3y"
}

conn.request(f"GET", f"/gasPrice/fromCity?city={city}", headers=headers)

res = conn.getresponse()
data = res.read()
data = json.loads(data.decode("utf-8"))
print("\rData fetched successfully!     ")


gasoline_price = float(data["result"]["gasoline"]) * 3.65
print("Fuel prices fetched")
if gasoline_price is None:
    print("Unable to fetch fuel prices. Please check your connection or API key.")
    exit()  # or set a default value


try:
    fuel_cons = float(input("What's your car's fuel consumption: liters per 100 km (l/100km)? "))
    if fuel_cons <= 0:
        raise ValueError("Fuel consumption must be a positive value.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()
finally:
    print("Your car's fuel consumption is " + str(fuel_cons) + " l/100km")


try:
    distance = float(input("What distance (km) do you want to travel?"))
    if distance <= 0:
        print("Sorry, enter a reasonable fuel consumption.")
except:
    print("Enter a decimal value only.")
finally:
    print("So the distance you want to travel is " + str(distance) + " kilometeres. Okay, let me cook")
def animate_loading():
    animation = ["|", "/", "-", "\\"]
    i = 0
    while not data_fetched:
        print(f"\rFetching data... {animation[i % len(animation)]}", end="")
        time.sleep(0.5)
        i += 1

cost = (fuel_cons / 100) * distance * gasoline_price
print(f"Estimated Trip Cost: {cost:.2f} Dhs")

emission_per_litre = 2.31  # kg CO2 per litre of petrol
emissions = (fuel_cons / 100) * distance * emission_per_litre
print(f"This trip will produce approximately {emissions:.2f} kg of CO2.")
