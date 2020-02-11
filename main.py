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

suggested_genes = results[selected -1]['associated_genes']

print()
print('SUGGESTED GENES')
print(suggested_genes)
#comment no genes found


from openpyxl import load_workbook


wb = load_workbook(filename = 'lifelabs.xlsx')
sheet_ranges = wb['Sheet1']
cells = sheet_ranges['B37:B4281']
genes = []
for cell in cells:
 value_stripped = cell[0].value.strip()
 if value_stripped:
  # strip all values (remove whitespace)
  values = list(v.strip() for v in value_stripped.split(','))
  # add to list of genes
  genes = genes + values

# convert to a set for fast lookup
genes = set(genes)
print(genes)

