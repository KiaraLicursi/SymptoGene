import requests

auth = "QWRtaW46YWRtaW4"
headers = {"Authorization": "Basic" +auth}
url = "http://localhost:8080/rest/vocabularies/hpo/suggest?input=bulb"

response = requests.get(url, headers=headers)
print(response.status_code)
