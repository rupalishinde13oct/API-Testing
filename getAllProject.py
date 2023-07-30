import requests

response = requests.get("https://rupalishinde13oct.atlassian.net/rest/api/3/project/search")
print(response.status_code)
print(response.json())
if response.status_code == 200:
    assert True
else:
    assert False