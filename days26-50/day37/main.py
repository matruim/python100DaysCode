import datetime

import requests

USERNAME = "matruim"
TOKEN = "aldksjasdkfjadflk"
GRAPH_ID = "readingtracker"
BASE_URL = "https://pixe.la"
CREATE_USER_ENDPOINT = f"{BASE_URL}/v1/users"
CREATE_USER_PARAMS = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
CREATE_GRAPH_ENDPOINT = f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs"
CREATE_GRAPH_PARAMS = {"id": GRAPH_ID, "name": "reading tracker", "unit": "books", "type": "int", "color": "ajisai"}

GRAPH_ENDPOINT = f"{CREATE_GRAPH_ENDPOINT}/{GRAPH_ID}"

headers = {"X-USER-TOKEN": TOKEN}


# res = requests.post(CREATE_USER_ENDPOINT, json=CREATE_USER_PARAMS)
# res = requests.post(CREATE_GRAPH_ENDPOINT, json=CREATE_GRAPH_PARAMS, headers={"X-USER-TOKEN": CREATE_USER_PARAMS["token"]})
# res = requests.post(GRAPH_ENDPOINT, json={"date": datetime.datetime.today().strftime("%Y%m%d"), "quantity": "5"}, headers={"X-USER-TOKEN": TOKEN})
# res = requests.put(f"{GRAPH_ENDPOINT}/20230816", headers=headers, json={"quantity": "15"})
res = requests.delete(f"{CREATE_USER_ENDPOINT}/{USERNAME}", headers=headers)
res.raise_for_status()
print(res.text)
print(res.json())
