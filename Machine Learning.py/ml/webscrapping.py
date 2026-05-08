import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
soup=BeautifulSoup(webpage,'lxml')

print(soup.prettify())


soup.find_all('h1')[0].text

for i in soup.find_all('h2'):
  print(i.text.strip())
  
for i in soup.find_all('p'):
  print(i.text.strip())
     

company=soup.find_all('div',class_='company-content-wrapper')
len(company) 
name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
how_old=[]
no_of_employee=[]

for i in company:

  name.append(i.find('h2').text.strip())
  rating.append(i.find('p',class_='rating').text.strip())
  reviews.append(i.find('a' , class_='review-count').text.strip())
  ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
  hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
  how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
  no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())

df=pd.DataFrame({'name':name,
   'rating':rating,
   'reviews':reviews,
   'company_type':ctype,
   'Head_Quarters':hq,
   'Company_Age':how_old,
   'No_of_Employee':no_of_employee,
   })

name

     
