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
print('POSSIBLE SYMPTOMS:\n')

i=1
for symptom in results :
	print ('[' + str(i) + ']' + symptom['name'])
	i+=1

print ('SELECT A SYMPTOM FROM THE LIST:')
selected = int(input())


if selected == 0 or selected > i:
		print ('INCORRECT INPUT')
		exit()



