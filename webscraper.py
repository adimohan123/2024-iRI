from bs4 import BeautifulSoup
import requests

response = requests.get('https://ninapro.hevs.ch/instructions/DB1.html')
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
soup.find_all('a')
urls = []
for link in soup.find_all('a'):
    s = link.get('href')
    type(s)
    if(s.endswith('.zip')):
       s = s[3:]
       hold =  'https://ninapro.hevs.ch/'  + s
       urls.append(hold)

print(urls)



