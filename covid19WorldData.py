from requests import get
from bs4 import BeautifulSoup
import csv
url='https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
url=get(url)
soup=BeautifulSoup(url.content,'html.parser')
containers=soup.find_all('tr')

head=[]
j=containers[0].find_all('th')
head=[j[0].text,j[1].text,j[2].text,j[3].text]
     
lists=[]   
for container in containers:
    con=container.find_all('td')
    try:
        case=con[1].text
        case=int(case.replace(',',''))
        death=con[2].text
        death=int(death.replace(',',''))
        list=[con[0].text,case,death,con[3].text]
    except:
          continue
    lists.append(list)

filename = "covidData.csv"
	
# writing to csv file 
with open(filename, 'w') as csvfile: 
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
		
	# writing the fields 
	csvwriter.writerow(head) 
		
	# writing the data rows 
	csvwriter.writerows(lists)        
