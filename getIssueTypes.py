import requests
header = {
    'accept': 'application/json'
}
response = requests.get("https://rupalishinde13oct.atlassian.net/rest/api/3/issuetype/project/10000", headers=header)
print(response.status_code)