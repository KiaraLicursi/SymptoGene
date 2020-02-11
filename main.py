import requests

auth = "QWRtaW46YWRtaW4"
headers = {"Authorization": "Basic" +auth}



print("Hello! Search for Symptoms:")
query = input()
print("SEARCHING...")
print(query)

url = "http://localhost:8080/rest/vocabularies/hpo/suggest?input=" + query

response = requests.get(url, headers=headers)

results = response.json()['rows']
print()
print('RESULTS:\n')
for symptom in results :
	print (symptom['name'])





