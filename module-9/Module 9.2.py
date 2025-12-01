#Drew Crockett
#11/30/25
#Module 9.2

import requests

# -------------------------------
# 1. Google Connection Test
# -------------------------------
print("=== Google Connection Test ===")
try:
    response = requests.get("http://www.google.com")
    print("Status Code:", response.status_code)
except Exception as e:
    print("Error connecting to Google:", e)

print("\n")

# -------------------------------
# 2. Astronauts API (Open Notify)
# -------------------------------
print("=== Astronauts API Test ===")
try:
    response = requests.get("http://api.open-notify.org/astros.json")
    print("Raw Response:", response.text)

    data = response.json()
    print("\nNumber of astronauts in space:", data["number"])
    print("Astronauts currently in space:")
    for person in data["people"]:
        print("-", person["name"], "on", person["craft"])
except Exception as e:
    print("Error retrieving astronaut data:", e)

print("\n")

# -------------------------------
# 3. Dog API (Random Dog Image)
# -------------------------------
print("=== Dog API Test ===")
try:
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    print("Raw Response:", response.text)

    data = response.json()
    print("\nRandom Dog Image URL:", data["message"])
except Exception as e:
    print("Error retrieving dog image:", e)
