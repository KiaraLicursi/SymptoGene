############################
#File Name: SymptoGene	   #
#Author: Kiara Licursi	   #
#Date: February 12th, 2020 #
#Project: Indu Capstone	   #
############################

import requests

#Used the Network function on DevTOOLS on Google Chrome to record the entire process of the api,
#Patient creation, symptom search, and gene acquisition
#This was done to discover which endpoint was being requested for the process above

auth = "QWRtaW46YWRtaW4"
#done via postman (which encodes it into base64), User: Admin, pass:admin

headers = {"Authorization": "Basic" +auth}
# defining dictionary and assigning it to the headers parameter

#copy pasted the endpoint and query to find the code needed when I log into the API
#into postman which converted the login into the auth code above

print("Hello! Search for Symptoms:") 
#prompts the user
query = input() 
#creates a variable and assigns a user input to it
print("SEARCHING...") 
#tells the user that the program is searching 
print(query) 
#prints the input

url = "http://localhost:8080/rest/vocabularies/hpo/suggest?input=" + query
#adds the query variable (which was entered by the user) into the query zone of the url

#url anatomy: server/endpoint/query string

response = requests.get(url, headers=headers)

#function argument 
#Utilizing the headers dictionary parameter from the requests library 
#Assigning the url's get request to the response variable

#Using the get request to retrive data from the url above.

results = response.json()['rows']
#json module organizes the symptom data structures into JSON strings, also kn0own as parsing
#json stands for javascript object notation
#assigning it to results variable
#rows are what they called it in the original api code

print()
#Execute the previous print command


print('POSSIBLE SYMPTOMS:\n')


i=1
#initialize the i variable
for symptom in results :
	print ('[' + str(i) + ']' + symptom['name']) #print a [#] next to the possible symptom
	i+=1    									#name is from the original api code
												#initialize i to go to the next index every iteration
print ('SELECT A SYMPTOM FROM THE LIST:')

selected = int(input())
#initialize integer input to variable selected
#input by the user, command already in python
if selected == 0 or selected > i:
		print ('INCORRECT INPUT')
		exit()
#if the user selects nothing or more than options, print incorrect input


if 'associated_genes' not in results[selected-1]:
	print ('NO RESULTS')
	exit()

suggested_genes = results[selected -1]['associated_genes']
#suggested_Genes variable holds a list of associated_genes from the api code
#it takes the (user input -1) from the list
#and assigns this result to suggested_genes
#selected (user input) - 1 since python reads 0 as 1 automatically


print()
print('SUGGESTED GENES')
print(suggested_genes)



#comment no genes found

'''

from openpyxl import load_workbook


wb = load_workbook(filename = 'lifelabs.xlsx') #connect excel file
sheet_ranges = wb['Sheet1'] #connect sheet 1
cells = sheet_ranges['B37:B4281'] #range in excel of genes we need assigned to variable cells
genes = [] #creating an empty list assigned to variable genes
for cell in cells: #assigning a variable cell within cells
 value_stripped = cell[0].value.strip() # local variable value_stripped:remove white space around cell values
 if value_stripped: #If cell value is stripped
  # strip all values (remove whitespace)
  values = list(v.strip() for v in value_stripped.split(',')) #list the genes in the cells
  # add to list of genes
  genes = genes + values

# convert to a set for fast lookup
genes = set(genes)
print(genes)
print(len(genes))
'''
