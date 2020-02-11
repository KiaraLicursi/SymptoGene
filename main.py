import requests

auth = "QWRtaW46YWRtaW4"
headers = {"Authorization": "Basic" +auth}
url = "http://localhost:8080/rest/vocabularies/hpo/suggest?input=" + query


print("Hello! Search for Symptoms:")
query = input()
print("searching...")
print(query)

response = requests.get(url, headers=headers)
print(response.json())



