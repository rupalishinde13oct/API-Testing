import pytest
import requests

def test_DemoTesting():
    header = {
        'Content-Type' : 'application/json'
    }

    base_url = "https://reqres.in"

    response = requests.get(url=base_url+"/api/users/2" , headers=header)
    assert response.status_code == 200
    print(response.json())

    # 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