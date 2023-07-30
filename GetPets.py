
import requests

header = {
    'accept': 'application/json'
}

response = requests.get("https://petstore.swagger.io/v2/store/inventory" , headers=header)
print(response.status_code)

jsonData = response.json()
print(jsonData)
print(jsonData['pending'])