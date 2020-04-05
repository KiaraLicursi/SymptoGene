############################
#File Name: SymptoGene	   #
#Author: Kiara Licursi	   #
#Date: March 25th, 2020 #
#Project: Indu Capstone	   #
############################

import requests
from openpyxl import load_workbook

#########################
## GET SUGGESTED GENES ##
#########################

auth = "QWRtaW46YWRtaW4"
headers = {"Authorization": "Basic" +auth}

print("Hello! Search for Symptoms:") 

query = input() 

print("SEARCHING...") 

print(query) 


url = "http://localhost:8080/rest/vocabularies/hpo/suggest?input=" + query


response = requests.get(url, headers=headers)

results = response.json()['rows']




print('POSSIBLE SYMPTOMS:\n')


i=1

for symptom in results :
	print ('[' + str(i) + ']' + symptom['name']) 
	i+=1

print('SELECT A SYMPTOM FROM THE LIST:')
selected = int(input())

if selected == 0 or selected > i:
		print('INCORRECT INPUT')
		exit()

if 'associated_genes' not in results[selected-1]:
	print ('NO RESULTS')
	exit()

suggested_genes = results[selected - 1]['associated_genes']

print()
print('SUGGESTED GENES')
print(suggested_genes)


length_sugg=len(suggested_genes)


print("Total amount of suggested genes to be tested:", len(suggested_genes)) #Prints the COUNT of the amount of genes that need to be tested


########## LABS ##########

wb = load_workbook(filename = 'labs.xlsx') 
labs = {}


##########################
## PARSE LIFELABS GENES ##
##########################

sheet_ranges = wb['LifeLabs']

cells = sheet_ranges['B5:B3902'] 

life_genes = [] 

for cell in cells: 
	value_stripped = cell[0].value.strip() 

	if value_stripped != '':
		values = [v.strip() for v in value_stripped.split(',')]
		life_genes += values

labs['LifeLabs'] = life_genes



############################
## PARSE CENTOGENES GENES ##
############################

sheet_ranges = wb['Centogene']

cells = sheet_ranges['B38:B363'] 

cento_genes = [] 

for cell in cells: 
	value_stripped = cell[0].value.strip() 

	if value_stripped != '':
		values = [v.strip() for v in value_stripped.split(',')]
		cento_genes += values

labs['Centogene'] = cento_genes


##########################
## PARSE BACKBONE GENES ##
##########################

sheet_ranges = wb['Backbone']

cells = sheet_ranges['B2:B5207'] 

back_genes = [] 

for cell in cells: 
	value_stripped = cell[0].value.strip() 

	if value_stripped != '':
		values = [v.strip() for v in value_stripped.split(',')]
		back_genes += values

labs['Backbone'] = back_genes



##################
## SHOW RESULTS ##
##################




def get_ratio(suggested_genes, lab_genes):
	# Convert to set for fast lookup and no duplicates
	lab_genes = set(lab_genes)
	remaining_genes = set()
	counter = 0
	
	
	
	for sg in suggested_genes:
		if sg in lab_genes:
			counter += 1
		else:
			remaining_genes.add(sg)
			
			
	

	#Returns the RATIO of the required genes vs those available at labs
	
	ratio = (counter/len(suggested_genes))
	return ratio, remaining_genes






# labs is dictionary like so:
# { name: list_of_genes }

for lab in labs:
	genes = labs[lab]
	ratio, remaining_genes = get_ratio(suggested_genes, genes)

	print("\n" + lab + " can test for " + str(ratio*100) + "% of the suggested genes, and cannot test for the following:")
	print (remaining_genes)

print("**Please note that Backbone tests each gene individually, and therefore is much more expensive. \n")




