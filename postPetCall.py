import requests

header = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

bodydata = {

  "id": 100,
  "petId": 1,
  "quantity": 2,
  "shipDate": "2023-07-28T18:17:26.432Z",
  "status": "placed",
  "complete": True

}
print("Before Update")
response = requests.post("https://petstore.swagger.io/v2/store/order" , headers=header , json=bodydata)
print(response.json())

print("After Update")

header = {
    'accept': 'application/json'

}

bodydata2 = {

  "id": 200,
  "petId": 1,
  "quantity": 2,
  "shipDate": "2023-07-28T18:17:26.432Z",
  "status": "placed",
  "complete": True

}
